import tempfile
from git import Repo

def clone_repo(repo_url):

    temp_dir = tempfile.mkdtemp()

    Repo.clone_from(
        repo_url,
        temp_dir,
        depth=1   # shallow clone
    )

    repo_name = repo_url.rstrip("/").split("/")[-1].replace(".git","")

    return temp_dir, repo_name