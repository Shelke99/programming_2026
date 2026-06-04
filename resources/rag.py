import os
import json
from pathlib import Path
from typing import List, Tuple

import numpy as np
from dotenv import load_dotenv
from google.oauth2 import service_account
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.documents.base import Document
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from flask_restful import Resource, request
import common.config as config
import pandas as pd
import logging
from datetime import datetime
# Load environment variables
load_dotenv()


def init_models():
    try:
        """Initialize models using Vertex AI with service account credentials."""
        # Load credentials from JSON file
        creds = service_account.Credentials.from_service_account_file(
            "cdesks-vertexai.json",
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )

        # Initialize LLM with Vertex AI
        model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            project="gc-proj-icapps-prd",
            credentials=creds,
            vertexai=True
        )

        # Initialize Embeddings with Vertex AI
        embeddings = GoogleGenerativeAIEmbeddings(
            model="gemini-embedding-001",
            project="gc-proj-icapps-prd",
            credentials=creds,
            vertexai=True,
        )
        return embeddings, model
    except Exception as e:
        logging.info(f"Error Occurred In init_models Function...{str(e)}")
        return ''

# Initialize components
embeddings, model = init_models()
vector_store = InMemoryVectorStore(embeddings)

# Conversation history
conversation_history: List[BaseMessage] = []


def ingest_json_records(records: list):
    try:
        """
        Ingest JSON records into the vector store with precomputed embeddings.
        """
        import uuid as uuid_lib
        import json
        import numpy as np

        ingested = 0

        for r in records:
            embedding = r.get("embedding")

            # ---- 1. Skip null embeddings
            if embedding is None:
                continue

            # ---- 2. Convert string embeddings → list
            if isinstance(embedding, str):
                try:
                    embedding = json.loads(embedding)
                except Exception:
                    continue

            # ---- 3. Ensure list
            if not isinstance(embedding, list) or len(embedding) == 0:
                continue

            # ---- 4. Convert to float + remove bad values
            try:
                vector = np.array(embedding, dtype=float)
            except Exception:
                continue

            # ---- 5. Reject NaNs / inf
            if np.isnan(vector).any() or np.isinf(vector).any():
                continue

            doc_id = str(uuid_lib.uuid4())

            vector_store.store[doc_id] = {
                "id": doc_id,
                "vector": vector.tolist(),  # store clean floats
                "text": r.get("content") or "",
                "metadata": {
                    "url": r.get("url", ""),
                    "domain": r.get("domain", ""),
                    "subdomain": r.get("subdomain", ""),
                    "title": r.get("title", ""),
                }
            }

            ingested += 1
        logging.info(f"Successfully ingested {ingested} valid documents into vector store.")

    except Exception as e:
        logging.info(f"Error Occurred In ingest_json_records Function...{str(e)}")
        return {"res_status": False, "msg": str(e)}


# Define the retrieval tool
@tool(response_format="content_and_artifact")
def retrieve_context(query: str) -> Tuple[str, List[Document]]:
    """Retrieve information to help answer a query."""
    try:
        retrieved_docs = vector_store.similarity_search(query, k=5)
        serialized = "\n\n".join(
            f"Source: {doc.metadata.get('title', 'Unknown')} ({doc.metadata.get('url', 'No URL')})\nContent: {doc.page_content}"
            for doc in retrieved_docs
        )
        return serialized, retrieved_docs
    except Exception as e:
        logging.info(f"Error Occurred In retrieve_context Function...{str(e)}")
        return '', []


SYSTEM_PROMPT = """You have access to a tool that retrieves context from documentation. Use the tool to help answer user queries.

### Role
You are the Website Assistant, an expert advisor. Your goal is to provide accurate, helpful, and concise information based strictly on the provided documentation.

### Operating Instructions
1. **Source Material First:** Use the provided context to answer all queries. If the answer is not contained within the context, politely state that you do not have that information.
2. **Markdown Integrity:** Use **bolding** for emphasis, `code blocks` for technical terms, and lists for complexity.
3. **Tone and Style:** Maintain a professional and friendly tone. Be concise.
4. **No Hallucinations:** Do not make up facts or features not in the context.
5. **Handling Ambiguity:** Ask clarifying questions if needed.

## Constraints
- Do not mention "VectorStore" or "retrieved documents."
- Present links as clickable Markdown links.

### Response Format
- Start with a direct answer.
- End with a brief, helpful follow-up question.
"""

tools = [retrieve_context]
agent = create_react_agent(model, tools, prompt=SYSTEM_PROMPT)


def process_query(query: str, json_data: list) -> str:
    """
    Process a query and return the response, maintaining conversation history.

    Args:
        query: User's question/query string
        json_data: List of records from JSON/DB containing url, domain,
                   subdomain, title, content, and embedding fields

    Returns:
        AI response string
    """
    # Clear existing vector store data and reingest
    vector_store._store = {}

    # Ingest JSON records into vector store
    ingest_json_records(json_data)

    # Add user message to conversation history
    conversation_history.append(HumanMessage(content=query))

    try:
        # Invoke agent with full conversation history
        response = agent.invoke({"messages": conversation_history})

        # Extract the last message from the agent
        ai_message = response["messages"][-1]

        # Add AI response to history
        conversation_history.append(ai_message)

        return {"res_status": True, "data": ai_message.content}
    except Exception as e:
        logging.error(f"Error Occurred in process_query Function...{str(e)}")
        return {"res_status": False, "msg": str(e)}



def clear_history() -> None:
    """Clear the conversation history."""
    conversation_history.clear()

def retrieve_embedded_data(domain, sub_domain):
    connection = None
    try:
        start_time = datetime.now()
        logging.info(f"In retrieve_embedded_data Function")
        db_start_time = datetime.now()
        connection = config.conn()
        db_established_time = datetime.now() - db_start_time
        logging.info('Database Connection Established')
        if "None" in str(connection):
            logging.info('Database Connection Failed')
            return {"res_status": False, "msg": "Database Connection Failed"}
        logging.info(f"Time Taken To Establish DB Connection...{db_established_time.total_seconds()} Seconds")

        query = f"SELECT * FROM web_bot.web_bot_scrape WHERE lower(domain)='{domain.lower()}' and lower(sub_domain)='{sub_domain.lower()}'"
        logging.info(f"Retrieve Query...{query}")
        df = pd.read_sql(query, connection)
        df = df[["domain", "sub_domain", "url", "title", "group_id", "embedding", "context", "metadata"]]
        df = df.rename(columns={"context": "content", "sub_domain": "subdomain"})
        dict_data = df.to_dict(orient="records")
        execution_time = datetime.now() - start_time
        logging.info(f'Retrieve Query API Completed In...{execution_time.total_seconds()} Seconds')
        return {"res_status": True, "data": dict_data}
    except Exception as e:
        logging.info(f"Error Occurred in retrieve_embedded_data Function...{str(e)}")
        return {"res_status": False, "msg": str(e)}
    finally:
        if connection:
            config.ConnectionPooling.postgres_pool['pool'].putconn(connection)


class WebsiteRag(Resource):
    def post(self):
        try:
            start_time = datetime.now()
            logging.info(f"In WebsiteRag Class")
            data = request.get_json()
            domain = data["domain"]
            sub_domain = data["sub_domain"]
            text = data["text"]
            result = retrieve_embedded_data(domain, sub_domain)
            if result["res_status"] == False:
                return result
            json_from_db = result["data"]

            answer = process_query(text, json_from_db)

            if answer["res_status"] == False:
                return answer
            if type(answer["data"]) == list:
                output = answer["data"][0]['text']
            else:
                output = answer["data"]
            execution_time = datetime.now() - start_time
            logging.info(f'Website Rag class Completed In...{execution_time.total_seconds()} Seconds')
            return {"res_status": True, "data": output}

        except Exception as e:
            logging.info(f"Error Occurred in WebsiteRag class...{str(e)}")
            return {"res_status": False, "msg": str(e)}

