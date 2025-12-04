import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert "Programming Class" in data


def test_signup_and_unregister():
    activity = "Chess Club"
    email = "testuser@mergington.edu"
    # Signup
    response = client.post(f"/activities/{activity}/signup?email={email}")
    assert response.status_code == 200
    assert f"Successfully signed up {email}" in response.json()["message"]
    # Duplicate signup should fail
    response = client.post(f"/activities/{activity}/signup?email={email}")
    assert response.status_code == 400
    # Unregister
    response = client.delete(f"/activities/{activity}/unregister?email={email}")
    assert response.status_code == 200
    assert f"Successfully removed {email}" in response.json()["message"]
    # Unregister again should fail
    response = client.delete(f"/activities/{activity}/unregister?email={email}")
    assert response.status_code == 400
