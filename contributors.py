import requests
import os

token = os.getenv("GITHUB_TOKEN")
repo= "AyhamAlsayyed/test-api-repo"

headers = {
    "Authorization": f"token {token}",
}

def get_contributors(repo):
    url = f"https://api.github.com/repos/{repo}/contributors"
    response = requests.get(url, headers=headers)
    return response.json()

contributors = get_contributors(repo)
#print(contributors)

for contributor in contributors:
    print(f"{contributor['login']} — {contributor['contributions']} contributions")