import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from books.models import Book


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user(db):
    user = User.objects.create_user(username="testuser", password="testpass123")
    return user


@pytest.fixture
def auth_client(api_client, create_user):
    # log in and get JWT token
    response = api_client.post("/api/token/", {
        "username": "testuser",
        "password": "testpass123"
    }, format="json")
    token = response.data["access"]
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client


@pytest.mark.django_db
def test_get_books_unauthorized(api_client):
    response = api_client.get("/books/")
    assert response.status_code == 401


@pytest.mark.django_db
def test_create_book(auth_client):
    data = {"title": "New Book", "author": "John Doe"}
    response = auth_client.post("/books/", data, format="json")
    assert response.status_code == 201
    assert response.data["title"] == "New Book"


@pytest.mark.django_db
def test_get_books_authorized(auth_client):
    # create a book first
    Book.objects.create(title="Sample Book", author="Jane Doe")
    response = auth_client.get("/books/")
    assert response.status_code == 200
    assert len(response.data) > 0


@pytest.mark.django_db
def test_update_book(auth_client):
    book = Book.objects.create(title="Old Title", author="Anon")
    url = f"/books/{book.id}/"
    response = auth_client.put(url, {"title": "Updated Title", "author": "Anon"}, format="json")
    assert response.status_code == 200
    assert response.data["title"] == "Updated Title"


@pytest.mark.django_db
def test_delete_book(auth_client):
    book = Book.objects.create(title="Delete Me", author="Anon")
    url = f"/books/{book.id}/"
    response = auth_client.delete(url)
    assert response.status_code == 204
    assert Book.objects.count() == 0
