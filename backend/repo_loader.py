import os
from git import Repo

def clone_repo(repo_url, local_path="data/repo"):
    """
    Clones a GitHub repository to a local directory.
    If the repository already exists, it will not clone again.
    """
    if os.path.exists(local_path):
        print("Repository already exists. Skipping clone.")
        return local_path

    os.makedirs(local_path, exist_ok=True)
    Repo.clone_from(repo_url, local_path)

    return local_path
