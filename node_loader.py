"""
Node Loader Module - Connects scrappy.py output to raggy.py RAG system.
"""
import json
from pathlib import Path

from raggy import process_query


DATA_DIR = Path(__file__).parent / "data"


def save_nodes(nodes: list, domain: str, subdomain: str) -> str:
    """Save scraper results to JSON file."""
    DATA_DIR.mkdir(exist_ok=True)
    file_path = DATA_DIR / f"{domain}_{subdomain}.json"
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(nodes, f, ensure_ascii=False, indent=2, default=str)
    
    return str(file_path)


def load_nodes(domain: str, subdomain: str) -> list:
    """Load nodes from JSON file."""
    file_path = DATA_DIR / f"{domain}_{subdomain}.json"
    
    with open(file_path, "r", encoding="utf-8") as f:
        nodes = json.load(f)
    
    return nodes


def load_content(nodes: list) -> str:
    """Extract and combine content from all nodes."""
    output = ""
    
    for node in nodes:
        output += node["content"] + "\n"
    
    return output


def query_data(query: str, domain: str, subdomain: str) -> str:
    """Main entry point - load nodes, get content, query RAG."""
    nodes = load_nodes(domain, subdomain)
    content = load_content(nodes)
    answer = process_query(query)
    
    return answer


if __name__ == "__main__":
    # Example usage
    from scrappy import WebScraper
    
    # Run scraper (use max_threads=1 for reliable results)
    print("Starting scraper...")
    scraper = WebScraper("https://httpbin.org", delay=0, max_threads=1)
    results = scraper.crawl()
    print(f"Scraper finished. Stats: crawled={scraper.stats['crawled']}, errors={scraper.stats['errors']}")
    
    # Save results
    domain = results[0]["domain"] if results else "unknown"
    subdomain = results[0]["subdomain"] if results else ""
    file_path = save_nodes(results, domain, subdomain)
    print(f"Saved {len(results)} nodes to: {file_path}")
    
    # Load and display content
    loaded_nodes = load_nodes(domain, subdomain)
    content = load_content(loaded_nodes)
    print(f"\nLoaded {len(loaded_nodes)} nodes")
    print(f"Combined content length: {len(content)} characters")
