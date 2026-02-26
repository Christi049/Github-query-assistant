from backend.code_reader import read_repository
from backend.code_parser import chunk_code
from backend.embeddings import embed_chunks
from backend.vector_store import create_collection, store_chunks

def index_repository(repo_path, collection_name):
    
    print("Reading repo...")
    docs = read_repository(repo_path)

    print("Chunking...")
    chunks = chunk_code(docs)

    print("Embedding...")
    embedded_chunks = embed_chunks(chunks)

    print("Creating DB (first time only)...")
    create_collection(collection_name)

    print("Storing embeddings...")
    store_chunks(embedded_chunks, collection_name)

    print("Indexing complete ✅")