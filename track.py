import json
import requests

def get_pull_requests(repo):
    url =f"https://api.github.com/repos/{repo}/pulls"
    response = requests.get(url)
    return response.json()

def get_contributors(repo):
    url = f"https://api.github.com/repos/{repo}/contributors"
    response = requests.get(url)
    return response.json()

repo= "octocat/Spoon-Knife"

contributors = get_contributors(repo)

for contributor in contributors:
    print(f"{contributor['login']} — {contributor['contributions']} contributions")

pull_requests = get_pull_requests(repo)

for pr in pull_requests:
    print(f"PR #{pr['number']}: {pr['title']} — by {pr['user']['login']} [{pr['state']}]")