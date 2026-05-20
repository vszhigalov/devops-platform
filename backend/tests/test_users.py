import uuid

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "DevOps Platform API is running",
    }


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["api"] == "healthy"


def test_create_user():
    unique_email = f"{uuid.uuid4()}@example.com"

    response = client.post(
        "/users/",
        json={
            "email": unique_email,
            "name": "John",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["email"] == unique_email
    assert data["name"] == "John"
