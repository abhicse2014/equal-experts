from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_octocat_gists():
    response = client.get("/octocat")
    assert response.status_code == 200
    data = response.json()
    assert data["user"] == "octocat"

def test_invalid_username():
    response = client.get("/invalid@user")
    assert response.status_code == 400

def test_user_not_found():
    response = client.get("/thisuserdoesnotexist123456789")
    assert response.status_code == 404
