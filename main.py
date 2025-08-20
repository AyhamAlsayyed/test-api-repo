import os

from Repo import Repos

token = os.getenv("GITHUB_TOKEN")

if not token:
    print("the token is not set")

# Example 1: (Uncomment to test repo creation/deletion)
"""
print("follow the steps to create your repo")
owner = input("Enter your UserName: ")
repo_name = input("Enter the repo name: ")
repo_description = input("Enter the repo description: ")

first_repo = Repos(owner, repo_name, repo_description)

first_repo.create(token)

repo2 = Repos("owner", "repo_name")

repo2.delete(token)
"""

repo = Repos("AyhamAlsayyed", "test-api-repo")

# Example 2: Contributors
contributors = repo.get_contributors()

for contributor in contributors:
    print(
        f"{contributor['login']} — {contributor['contributions']} contributions"
    )

# Example 3: Pull Requests
pull_requests = repo.get_pull_requests()

for pr in pull_requests:
    print(
        f"PR #{pr['number']}: {pr['title']} — by {pr['user']['login']} [{pr['state']}]"
    )
