#to extract required files from cloned repo 
import os

SUPPORTED_EXTENSIONS = [".py", ".js", ".ts", ".java", ".cpp", ".c", ".html", ".css"]

def read_repository(repo_path):
    documents = []

    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if any(file.endswith(ext) for ext in SUPPORTED_EXTENSIONS):
                full_path = os.path.join(root, file)

                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()

                    documents.append({
                        "file_path": full_path,
                        "content": content
                    })

                except Exception as e:
                    print("Error reading:", full_path)

    return documents
