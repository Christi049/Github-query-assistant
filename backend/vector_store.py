from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct
from backend.embeddings import embed_query
import os
import uuid


# persistent local database
client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)

# ---------- Create DB ----------
def create_collection(collection_name):
    collections = [c.name for c in client.get_collections().collections]

    if collection_name in collections:
        client.delete_collection(collection_name=collection_name)

    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    )

# ---------- Store ----------
def store_chunks(chunks, collection_name):
    """
    Expects chunks ALREADY containing embeddings
    (embedding created in embeddings.py)
    """

    points = []

    for chunk in chunks:
        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=chunk["embedding"],
                payload={
                    "content": chunk["content"],
                    "file_path": chunk["file_path"],
                    "start_line": chunk["start_line"],
                    "end_line": chunk["end_line"],
                },
            )
        )

    client.upsert(collection_name=collection_name, points=points)


# ---------- Search ----------
def search(question, collection_name, k=3):

    query_vector = embed_query(question)

    results = client.query_points(
        collection_name=collection_name,
        query=query_vector,
        limit=k,
    )

    return [hit.payload for hit in results.points]

