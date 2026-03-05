from backend.code_reader import read_repository
from backend.code_parser import chunk_code
from backend.embeddings import embed_chunks
from backend.vector_store import create_collection, store_chunks, collection_exists


def index_repository(repo_path, collection_name):

    # 🚨 Skip if already indexed
    if collection_exists(collection_name):
        print("Already indexed. Skipping.")
        return

    print("Reading repo...")
    docs = read_repository(repo_path)

    print("Chunking...")
    chunks = chunk_code(docs)

    print("Total chunks created:", len(chunks))

    print("Embedding...")
    embedded_chunks = embed_chunks(chunks,repo_path)

    print("Creating collection...")
    create_collection(collection_name)

    print("Storing embeddings...")
    store_chunks(embedded_chunks, collection_name)

    print("Indexing complete ✅")