from backend.code_reader import read_repository
from backend.code_parser import chunk_code
from backend.vector_store import create_collection, store_chunks, search

repo_path = "data/repo"

docs = read_repository(repo_path)
chunks = chunk_code(docs)

print("Creating vector DB...")
create_collection()

print("Storing embeddings...")
store_chunks(chunks)

print("\nAsk a question:")
results = search("Where is HTTP request handled?")

for r in results:
    print("\n--- MATCH ---")
    print(r["file_path"], f"(lines {r['start_line']}-{r['end_line']})")
    print(r["content"][:300])
