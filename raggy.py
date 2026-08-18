import os
from pathlib import Path
from typing import List, Tuple

from dotenv import load_dotenv
from google.oauth2 import service_account
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.documents.base import Document
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

# Load environment variables
load_dotenv()

def init_models():
    """Initialize models using Vertex AI with service account credentials."""
    # Load credentials from JSON file
    creds = service_account.Credentials.from_service_account_file(
        "cdesks-vertexai.json",
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    
    # Initialize LLM with Vertex AI
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        project="cdesks-vertex",
        credentials=creds,
        vertexai=True
    )
    
    # Initialize Embeddings with Vertex AI
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        project="cdesks-vertex",
        credentials=creds,
        vertexai=True,
    )
    
    return embeddings, model

# Initialize components
embeddings, model = init_models()
vector_store = InMemoryVectorStore(embeddings)

DOCS_PATH = Path(__file__).parent.joinpath("docs")

def load_documents(docs_path: Path) -> List[Document]:
    """Load documents from the specified directory."""
    docs = []
    if not docs_path.exists():
        print(f"Warning: Documents directory {docs_path} does not exist.")
        return docs

    print(f"Loading documents from: {docs_path}")
    for file_path in docs_path.iterdir():
        if file_path.is_file():
            try:
                content = file_path.read_text(encoding="utf-8")
                docs.append(
                    Document(page_content=content, metadata={"file_name": file_path.name})
                )
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    return docs

# Ingest documents
documents = load_documents(DOCS_PATH)
if documents:
    vector_store.add_documents(documents)
    print(f"Successfully indexed {len(documents)} documents.")

# Define the retrieval tool
@tool(response_format="content_and_artifact")
def retrieve_context(query: str) -> Tuple[str, List[Document]]:
    """Retrieve information to help answer a query."""
    retrieved_docs = vector_store.similarity_search(query, k=5)
    serialized = "\n\n".join(
        f"Source: {doc.metadata.get('file_name', 'Unknown')}\nContent: {doc.page_content}" 
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs

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

# Conversation history
conversation_history: List[BaseMessage] = []

def process_query(query: str) -> str:
    """Process a query and return the response, maintaining conversation history."""
    conversation_history.append(HumanMessage(content=query))

    try:
        # Invoke agent with full conversation history
        response = agent.invoke({"messages": conversation_history})
        
        # Extract the last message from the agent
        ai_message = response["messages"][-1]
        
        # Add AI response to history
        conversation_history.append(ai_message)
        
        return ai_message.content
        
    except Exception as e:
        print(f"Error during agent invocation: {e}")
        return "I'm sorry, I encountered an error while processing your request."

def clear_history() -> None:
    """Clear the conversation history."""
    conversation_history.clear()

if __name__ == "__main__":
    print("\nChat started. Type 'exit' or 'quit' to end, 'clear' to reset history.\n")
    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("exit", "quit"):
                break
            if user_input.lower() == "clear":
                clear_history()
                print("Conversation history cleared.\n")
                continue

            result = process_query(user_input)
            print(f"\nAssistant: {result[0]['text']}\n")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")
