from sentence_transformers import SentenceTransformer

# Load once (global)
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text: str):
    """Convert text into embedding vector"""
    return model.encode(text).tolist()

def embed_chunks(chunks):
    """Add embeddings to each chunk"""
    for chunk in chunks:
        chunk["embedding"] = embed_text(chunk["content"])
    return chunks

def embed_query(query: str):
    return model.encode(query).tolist()