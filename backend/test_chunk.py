from backend.code_reader import read_repository
from backend.code_parser import chunk_code

repo_path = "data/repo"

docs = read_repository(repo_path)
chunks = chunk_code(docs)

print("Total files:", len(docs))
print("Total chunks:", len(chunks))

print("\nFirst chunk:\n")
print("File:", chunks[0]["file_path"])
print("Lines:", chunks[0]["start_line"], "-", chunks[0]["end_line"])
print(chunks[0]["content"][:500])
