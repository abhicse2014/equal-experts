from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_octocat_gists():
    """
    Should return gists for a valid user (octocat)
    """
    response = client.get("/octocat")

    assert response.status_code == 200

    data = response.json()
    assert data["user"] == "octocat"
    assert isinstance(data["gists"], list)


def test_invalid_username():
    """
    Should return 400 for invalid username format
    """
    response = client.get("/invalid@user")

    assert response.status_code == 400


def test_user_not_found():
    """
    Should return 404 for non-existing user
    """
    response = client.get("/thisuserdoesnotexist123456789")

    assert response.status_code == 404