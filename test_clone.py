from backend.repo_loader import clone_repo

repo_url = "https://github.com/psf/requests"  # example repo
path = clone_repo(repo_url)

print("Repository cloned at:", path)
