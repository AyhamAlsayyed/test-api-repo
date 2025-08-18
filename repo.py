import requests

class repos:

    def __init__(self, repo_owner= None, repo_name= None, description= None):
        self.repo_name = repo_name
        self.repo_owner = repo_owner
        self.repo_description = description
        
    def repo_creation(self, token, repo_owner= None, repo_name= None,repo_description= None):
        url = "https://api.github.com/user/repos"

        headers = {
            "Authorization": f"token {token}",
        }

        data = {
            "name": repo_name or self.repo_name,
            "description": repo_description or self.repo_description,
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 201:
            print("repo created")
            self.repo_name = repo_name or self.repo_name
            self.repo_owner = repo_owner or self.repo_owner
            self.repo_description = repo_description or self.repo_description

        else:
            print(f"failed to creat a repo: {response.status_code}")
            print(response.json())

    def repo_deletion(self, token):
        url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}"
        
        headers = {
            "Authorization": f"token {token}",
        }
        
        response = requests.delete(url, headers=headers)
        
        if response.status_code == 204:
            print(f"Repository '{self.repo_owner}/{self.repo_name}' deleted successfully.")
        elif response.status_code == 404:
            print("Repository not found or you don't have permission to delete it.")
        else:
            print(f"Failed to delete repository: {response.status_code}")
            print(response.json())

    def repo_info(self):
        print(f"repo name {self.repo_name}")
        print(f"repo's owner {self.repo_owner}")
        print(f"repo's description {self.repo_description}")


    def get_pull_requests(self):
        if not self.repo_owner or  not self.repo_name:
            print("the repo don't have a an owner or a name")
            return 
        url =f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/pulls"

        response = requests.get(url)
        return response.json()

    def get_contributors(self):
        if not self.repo_owner or  not self.repo_name:
            print("the repo don't have a an owner or a name")
            return
        url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/contributors"
        response = requests.get(url)
        return response.json()