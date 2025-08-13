import json
import requests
'''
import os

token = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"token {token}",
}
'''
repo= "octocat/Spoon-Knife"

def get_contributors(repo):
    url = f"https://api.github.com/repos/{repo}/contributors"
    response = requests.get(url)
    return response.json()

contributors = get_contributors(repo)

for contributor in contributors:
    print(f"{contributor['login']} — {contributor['contributions']} contributions")

def get_pull_requests(repo):
    url =f"https://api.github.com/repos/{repo}/pulls"
    response = requests.get(url)
    return response.json()

pull_requests = get_pull_requests(repo)

for pr in pull_requests:
    print(f"PR #{pr['number']}: {pr['title']} — by {pr['user']['login']} [{pr['state']}]")