from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from app.github import get_user_gists
from app.exceptions import (
    InvalidUsernameError,
    UserNotFoundError,
    GitHubAPIError
)
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="GitHub Gists API")


# ✅ IMPORTANT: define this FIRST
@app.get("/favicon.ico")
def favicon():
    return Response(status_code=204)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/{username}")
def fetch_gists(username: str):
    try:
        logger.info(f"Fetching gists for user: {username}")

        gists = get_user_gists(username)

        return {
            "user": username,
            "total_gists": len(gists),
            "gists": gists
        }

    except InvalidUsernameError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except GitHubAPIError:
        raise HTTPException(status_code=502, detail="Upstream service error")
