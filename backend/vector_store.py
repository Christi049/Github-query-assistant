from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct
from backend.embeddings import embed_query
import uuid

COLLECTION_NAME = "code_chunks"

# persistent local database
client = QdrantClient(path="backend/qdrant_storage")


# ---------- Create DB ----------
def create_collection():
    collections = [c.name for c in client.get_collections().collections]

    if COLLECTION_NAME not in collections:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE),
        )


# ---------- Store ----------
def store_chunks(chunks):
    """
    Expects chunks ALREADY containing embeddings
    (embedding created in embeddings.py)
    """

    points = []

    for chunk in chunks:
        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=chunk["embedding"],  # <-- IMPORTANT: no encoding here
                payload={
                    "content": chunk["content"],
                    "file_path": chunk["file_path"],
                    "start_line": chunk["start_line"],
                    "end_line": chunk["end_line"],
                },
            )
        )

    client.upsert(collection_name=COLLECTION_NAME, points=points)


# ---------- Search ----------
def search(question, k=3):
    """
    Expects already embedded query vector
    """
    query_vector = embed_query(question)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=k,
    )

    return [hit.payload for hit in results.points]
