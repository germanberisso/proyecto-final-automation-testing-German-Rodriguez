import pytest
import requests
from unittest.mock import patch

BASE_URL = "https://reqres.in/api"

# Fixture para usuario temporal
@pytest.fixture(params=[
    {"name": "TempUser0", "job": "QA Automation"},
    {"name": "TempUser1", "job": "Tester"},
    {"name": "TempUser2", "job": "DevOps"}
])
def temp_user(request):
    return request.param


# Mock para GET /users
@pytest.fixture
def mock_get_users():
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "page": 2,
            "per_page": 3,
            "total": 12,
            "total_pages": 4,
            "data": [
                {"id": 4, "email": "eve.holt@reqres.in", "first_name": "Eve", "last_name": "Holt"},
                {"id": 5, "email": "charles.morris@reqres.in", "first_name": "Charles", "last_name": "Morris"},
                {"id": 6, "email": "tracey.ramos@reqres.in", "first_name": "Tracey", "last_name": "Ramos"}
            ]
        }
        yield mock_get


# Mock para POST /users
@pytest.fixture
def mock_create_user():
    with patch("requests.post") as mock_post:
        def fake_post(url, json):
            mock_response = requests.models.Response()
            mock_response.status_code = 201
            mock_response._content = str.encode(
                f'{{"id": "123", "name": "{json["name"]}", "job": "{json["job"]}"}}'
            )
            return mock_response
        mock_post.side_effect = fake_post
        yield mock_post

# Mock para DELETE /users
@pytest.fixture
def mock_delete_user():
    with patch("requests.delete") as mock_delete:
        mock_delete.return_value.status_code = 204
        yield mock_delete


# TESTS

def test_get_users(mock_get_users):
    response = requests.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0

def test_post_create_user(temp_user, mock_create_user):
    response = requests.post(f"{BASE_URL}/users", json=temp_user)
    assert response.status_code == 201
    result = response.json()
    assert result["name"] == temp_user["name"]
    assert result["job"] == temp_user["job"]

def test_delete_user(mock_delete_user):
    user_id = 123
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 204