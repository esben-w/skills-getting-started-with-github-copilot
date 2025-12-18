import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Mergington High School" in response.text

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    # Use a test activity and email
    activity = "Chess Club"
    email = "testuser@example.com"
    # Signup
    signup_response = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert signup_response.status_code in (200, 201)
    # Unregister
    unregister_response = client.post(f"/activities/{activity}/unregister", params={"email": email})
    assert unregister_response.status_code in (200, 201, 404)  # 404 if not found
