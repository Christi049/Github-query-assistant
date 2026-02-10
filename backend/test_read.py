from backend.code_reader import read_repository

repo_path = "data/repo"

docs = read_repository(repo_path)

print("Total files read:", len(docs))
print("\nSample file:\n")
print(docs[0]["file_path"])
print(docs[0]["content"][:500])
