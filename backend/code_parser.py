#chunking code files
import re

CHUNK_SIZE = 40   # lines per chunk
OVERLAP = 10      # overlapping lines (keeps context)

def chunk_code(documents):
    chunks = []

    for doc in documents:
        lines = doc["content"].split("\n")

        start = 0
        while start < len(lines):
            end = start + CHUNK_SIZE
            chunk_lines = lines[start:end]

            chunk_text = "\n".join(chunk_lines)

            chunks.append({
                "content": chunk_text,
                "file_path": doc["file_path"],
                "start_line": start + 1,
                "end_line": min(end, len(lines))
            })

            start += CHUNK_SIZE - OVERLAP

    return chunks
