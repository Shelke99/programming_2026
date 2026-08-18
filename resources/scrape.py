import json
import logging
import re
import time
import threading
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from uuid import uuid4
from google.oauth2 import service_account
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from flask_restful import Resource
from flask import request
from common import config as config
import  datetime



def get_domain_name(url: str) -> str:
    """
    Returns the domain name (e.g., 'example' from blog.api.example.com)
    """
    parsed = urlparse(url)
    host = parsed.hostname

    if not host:
        return ""

    parts = host.split(".")
    if len(parts) < 2:
        return host  # localhost or invalid domain

    return parts[-2]


def get_subdomain_name(url: str) -> str:
    """
    Returns the subdomain (e.g., 'blog.api' from blog.api.example.com)
    """
    parsed = urlparse(url)
    host = parsed.hostname

    if not host:
        return ""

    parts = host.split(".")
    if len(parts) <= 2:
        return ""  # no subdomain

    return ".".join(parts[:-2])


creds = service_account.Credentials.from_service_account_file(
    "cdesks-vertexai.json",
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    project="gc-proj-icapps-prd",
    credentials=creds,
    vertexai=True,
)


class WebScraper:
    def __init__(
            self,
            domain,
            delay=0,
            max_threads=1,

    ):
        self.domain = domain if domain.startswith("http") else f"https://{domain}"
        self.base_netloc = urlparse(self.domain).netloc
        self.visited = set()
        self.to_visit = deque([self.domain])
        self.group_id = str(uuid4())
        self.results = []
        # Create a subfolder for the domain inside output_dir

        self.delay = delay
        self.max_threads = max_threads
        self.stats = {
            "crawled": 0,
            "errors": 0,
            "skipped": 0,
            "start_time": None,
            "end_time": None,
        }
        self.lock = threading.Lock()
        self.log_entries = []
        self.output = {}

    def sanitize_filename(self, name):

        name = re.sub(r"[^a-zA-Z0-9_\-]", "_", name.strip().replace(" ", "_"))
        return name[:100]  # limit filename length

    def get_filename(self, url, soup):

        h1 = soup.find("h1")
        if h1 and h1.get_text(strip=True):
            base = self.sanitize_filename(h1.get_text(strip=True))
        else:
            path = urlparse(url).path.strip("/") or "index"
            base = self.sanitize_filename(path.replace("/", "_"))
        return f"{base}.md"

    def fetch_and_save(self, url):
        try:
            resp = requests.get(url, timeout=10)  # fetch html file from server
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")
            h1 = soup.find("h1")
            title_tag = soup.find("title")

            if h1 and h1.get_text(strip=True):
                title_text = h1.get_text(strip=True)
            elif title_tag:
                title_text = title_tag.get_text(strip=True)
            else:
                title_text = ""

            md_content = md(str(soup))
            embedding = embeddings.embed_query(md_content)
            # self.output[url] = {
            #     "title": title.get_text(stripe="True") if h1 else " ",
            #     "content": md_content,
            #     # "url": url,
            # }
            self.results.append({
                "url": url,
                "domain": get_domain_name(url),
                "sub_domain": get_subdomain_name(url),
                "title": title_text,
                "context": md_content,
                "embedding": embedding,
                "metadata": {"date": datetime.datetime.now()},
                "group_id": self.group_id,

            })

            self.stats["crawled"] += 1
            # Extract and queue new links
            for link in soup.find_all("a", href=True):
                abs_url = urljoin(str(url), str(link["href"]))
                parsed = urlparse(abs_url)
                if parsed.netloc == self.base_netloc and abs_url not in self.visited:
                    with self.lock:
                        if abs_url not in self.visited:
                            self.to_visit.append(abs_url)
            return True
        except Exception as e:
            self.log(f"ERROR: {url} - {e}")
            self.stats["errors"] += 1
            return False


    def log(self, message):

        with self.lock:
            self.log_entries.append(message)
    def crawl_single_thread(self):

        while self.to_visit:
            url = self.to_visit.popleft()
            with self.lock:
                if url in self.visited:
                    self.stats["skipped"] += 1
                    continue
                self.visited.add(url)
            self.fetch_and_save(url)
            if self.delay:
                time.sleep(self.delay)

    def crawl_multi_thread(self):

        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            futures = []
            while self.to_visit or futures:
                while self.to_visit and len(futures) < self.max_threads:
                    url = self.to_visit.popleft()
                    with self.lock:
                        if url in self.visited:
                            self.stats["skipped"] += 1
                            continue
                        self.visited.add(url)
                    futures.append(executor.submit(self.fetch_and_save, url))
                    if self.delay:
                        time.sleep(self.delay)
                # Remove completed futures
                futures = [f for f in futures if not f.done()]

    def crawl(self):
        self.stats["start_time"] = time.time()
        if self.max_threads > 1:
            self.crawl_multi_thread()
        else:
            self.crawl_single_thread()

        return self.results

    def show_stats(self):
        total_time = self.stats["end_time"] - self.stats["start_time"]
        print("\n--- Crawl Statistics ---")
        print(f"Total pages crawled: {self.stats['crawled']}")
        print(f"Total errors: {self.stats['errors']}")
        print(f"Total skipped: {self.stats['skipped']}")
        print(f"Total time: {total_time:.2f} seconds")

class WebsiteScrape(Resource):
    def post(self):
        db_conn = None
        try:
            start_time = datetime.datetime.now()
            logging.info(f"In Website Scrape Class")
            data = request.get_json()
            table_name = "web_bot.web_bot_scrape"
            url = data["url"]
            user_name = data["user_name"]
            domain = data["domain"]
            sub_domain = data["sub_domain"]

            db_start_time = datetime.datetime.now()
            db_conn = config.conn()
            db_established_time = datetime.datetime.now() - db_start_time
            logging.info('Database Connection Established')
            if "None" in str(db_conn):
                logging.info('Database Connection Failed')
                return {"res_status": False, "msg": "Database Connection Failed"}
            logging.info(f"Time Taken To Establish DB Connection...{db_established_time.total_seconds()} Seconds")

            scraper = WebScraper(
                url, delay=0, max_threads=6
            )

            results = scraper.crawl()
            print(results[0])
            if results:
                list(map(lambda x: x.update({"created_by": user_name, "domain": domain, "sub_domain": sub_domain}),
                         results))
                columns = [
                    "url", "domain", "sub_domain", "title",
                    "context", "embedding", "metadata",
                    "group_id", "created_by"
                ]
                list(map(
                    lambda r: r.update({
                        "metadata": json.dumps(r["metadata"], default=str)
                        if isinstance(r.get("metadata"), (dict, list)) else r.get("metadata")
                    }),
                    results
                ))

                values = [[row.get(col) for col in columns] for row in results]
                column_names = ", ".join(columns)
                placeholders = ", ".join(["%s"] * len(columns))

                query = f"INSERT INTO {table_name}({column_names}) VALUES({placeholders})"
                logging.info(f"Insert Query...{query}")
                cursor = db_conn.cursor()
                cursor.executemany(query, values)
                db_conn.commit()
                execution_time = datetime.datetime.now() - start_time
                logging.info(f'Insert Query API Completed In...{execution_time.total_seconds()} Seconds')
                return {"res_status": True, "msg": "Data Inserted Successfully"}
            else:
                return {"res_status": False, "msg": "No Content Found to Insert"}
        except Exception as e:
            logging.error(f"Error Occurred While Scraping the Site...{str(e)}")
            return {"res_status": False, "msg": str(e)}
        finally:
            if db_conn:
                config.ConnectionPooling.postgres_pool['pool'].putconn(db_conn)


