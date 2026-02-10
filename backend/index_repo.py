from backend.code_reader import read_repository
from backend.code_parser import chunk_code
from backend.embeddings import embed_chunks
from backend.vector_store import create_collection, store_chunks

repo_path = "data/repo"

print("Reading repo...")
docs = read_repository(repo_path)

print("Chunking...")
chunks = chunk_code(docs)

print("Embedding...")
embedded_chunks = embed_chunks(chunks)

print("Creating DB (first time only)...")
create_collection()

print("Storing embeddings...")
store_chunks(embedded_chunks)

print("Indexing complete ✅")
