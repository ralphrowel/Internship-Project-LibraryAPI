import pytest
from rest_framework.test import APIClient
from users.models import User
from books.models import Book
from permissions.roles import LIBRARIAN, ADMIN

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_librarian_user(db):
    user = User.objects.create_user(
        username="librarian",
        password="testpass123",
        role=LIBRARIAN
    )
    return user

@pytest.fixture
def create_admin_user(db):
    user = User.objects.create_user(
        username="admin",
        password="testpass123",
        role=ADMIN
    )
    return user

@pytest.fixture
def auth_client_librarian(api_client, create_librarian_user):
    response = api_client.post("/api/token/", {
        "username": "librarian",
        "password": "testpass123"
    }, format="json")
    token = response.data["access"]
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client

@pytest.fixture
def auth_client_admin(api_client, create_admin_user):
    response = api_client.post("/api/token/", {
        "username": "admin",
        "password": "testpass123"
    }, format="json")
    token = response.data["access"]
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client

@pytest.mark.django_db
def test_get_books_unauthorized(api_client):
    response = api_client.get("/api/books/")
    assert response.status_code == 200  # AllowAny in list

@pytest.mark.django_db
def test_create_book(auth_client_librarian):
    data = {"title": "New Book", "author": "John Doe"}
    response = auth_client_librarian.post("/api/books/", data, format="json")
    assert response.status_code == 201
    assert response.data["title"] == "New Book"

@pytest.mark.django_db
def test_update_book(auth_client_librarian):
    book = Book.objects.create(title="Old Title", author="Anon")
    url = f"/api/books/{book.id}/"
    response = auth_client_librarian.put(url, {"title": "Updated Title", "author": "Anon"}, format="json")
    assert response.status_code == 200
    assert response.data["title"] == "Updated Title"

@pytest.mark.django_db
def test_delete_book(auth_client_admin):
    book = Book.objects.create(title="Delete Me", author="Anon")
    url = f"/api/books/{book.id}/"
    response = auth_client_admin.delete(url)
    assert response.status_code == 204
    assert Book.objects.count() == 0
