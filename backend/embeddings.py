from sentence_transformers import SentenceTransformer
import os

# Load once (global)
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text: str):
    """Convert text into embedding vector"""
    return model.encode(text).tolist()

def embed_chunks(chunks, repo_path):
    """Add embeddings to each chunk using batch encoding"""

    texts = []

    for chunk in chunks:
        relative_path = os.path.relpath(chunk["file_path"], repo_path)
        text_to_embed = f"File:{relative_path}\n{chunk['content']}"
        texts.append(text_to_embed)

    print(f"Embedding {len(texts)} chunks...")

    embeddings = model.encode(
        texts,
        batch_size=128,
        show_progress_bar=True
    )

    for chunk, emb in zip(chunks, embeddings):
        chunk["embedding"] = emb.tolist()

    return chunks

def embed_query(query: str):
    return model.encode(query).tolist()