import requests


class Repos:
    """A class to manage GitHub repos via the API."""

    def __init__(self, token, repo_owner=None, repo_name=None, description=None):
        """
        Initialize a Repos object.

        Args:
            token (str): GitHub access token.
            repo_owner (str): GitHub username of the repo owner.
            repo_name (str): Name of the repo.
            description (str): Description of the repo.
        """
        self.token = token
        self.repo_name = repo_name
        self.repo_owner = repo_owner
        self.repo_description = description

    def create(self, token, repo_owner=None, repo_name=None, repo_description=None):
        """Create a new repo using the API."""
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
            self.repo_name = repo_name or self.repo_name
            self.repo_owner = repo_owner or self.repo_owner
            self.repo_description = repo_description or self.repo_description
            return {"status": "success", "massage": "repo created."}
        else:
            return {
                "status": "error",
                "code": response.status_code,
                "details": response.json(),
            }

    def delete(self, token):
        """Delete the repo."""
        url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}"

        headers = {
            "Authorization": f"token {token}",
        }

        response = requests.delete(url, headers=headers)

        if response.status_code == 204:
            return {
                "status": "success",
                "message": f"Repository '{self.repo_owner}/{self.repo_name}' deleted.",
            }
        elif response.status_code == 404:
            return {
                "status": "error",
                "message": "Repository not found or no permission.",
            }
        else:
            return {
                "status": "error",
                "code": response.status_code,
                "details": response.json(),
            }

    def get(self):
        """return repo information."""
        return {
            "name": self.repo_name,
            "owner": self.repo_owner,
            "description": self.repo_description,
        }

    def get_pull_requests(self):
        """Fetch pull requests of the repo."""
        if not self.repo_owner or not self.repo_name:
            print("the repo don't have a an owner or a name")
            return
        url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/pulls"

        response = requests.get(url)
        return response.json()

    def get_contributors(self):
        """Fetch contributors of the repo."""
        if not self.repo_owner or not self.repo_name:
            print("the repo don't have a an owner or a name")
            return
        url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/contributors"
        response = requests.get(url)
        return response.json()
