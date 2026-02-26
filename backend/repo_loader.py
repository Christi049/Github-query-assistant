#handle conflicts -in case multiple users are using app at the same time
import tempfile
from git import Repo

def clone_repo(repo_url):
    temp_dir = tempfile.mkdtemp()
    Repo.clone_from(repo_url, temp_dir)

    # extract repo name
    repo_name = repo_url.rstrip("/").split("/")[-1]

    return temp_dir, repo_name