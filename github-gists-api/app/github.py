import requests
from app.exceptions import InvalidUsernameError, UserNotFoundError, GitHubAPIError

GITHUB_API = "https://api.github.com"

def get_user_gists(username: str):
    if not username.isalnum():
        raise InvalidUsernameError("Invalid username format")

    url = f"{GITHUB_API}/users/{username}/gists"

    try:
        response = requests.get(url, timeout=3)

        if response.status_code == 404:
            raise UserNotFoundError("User not found")

        response.raise_for_status()
        data = response.json()

        return [
            {
                "id": gist.get("id"),
                "description": gist.get("description"),
                "url": gist.get("html_url")
            }
            for gist in data
        ]

    except requests.exceptions.Timeout:
        raise GitHubAPIError("GitHub timeout")
    except requests.exceptions.RequestException:
        raise GitHubAPIError("GitHub API error")
