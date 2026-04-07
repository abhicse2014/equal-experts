from fastapi import FastAPI, HTTPException
from app.github import get_user_gists
from app.exceptions import (
    InvalidUsernameError,
    UserNotFoundError,
    GitHubAPIError
)

app = FastAPI(title="GitHub Gists API")

@app.get("/{username}")
def fetch_gists(username: str):
    try:
        gists = get_user_gists(username)
        return {"user": username, "total_gists": len(gists), "gists": gists}
    except InvalidUsernameError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except GitHubAPIError:
        raise HTTPException(status_code=502, detail="Upstream service error")
