import os
import requests

token = os.getenv("GITHUB_TOKEN")

username = "AyhamAlsayyed" 
repo_name = "test-api-repo"
description = "Created via GitHub API"

url = "https://api.github.com/user/repos"

headers = {
    "Authorization": f"token {token}",
}

data = {
    "name": repo_name,
    "description": description,
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print("repo created")
    print(" URL:", response.json()["html_url"])
else:
    print(f"failed to creat a repo: {response.status_code}")
    print(response.json())
