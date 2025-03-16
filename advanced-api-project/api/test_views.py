from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Book

class BookAPITestCase(APITestCase):
    """ Test suite for the Book API """

    def setUp(self):
        """ Set up test user and sample book data """
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.force_authenticate(user=self.user)

        self.book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            publication_year=2023
        )

        self.book_url = f"/api/books/{self.book.id}/"
        self.list_url = "/api/books/"

    def test_create_book(self):
        """ Test creating a book """
        data = {
            "title": "New Book",
            "author": "Jane Doe",
            "publication_year": 2024
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    def test_list_books(self):
        """ Test retrieving all books """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ensure only one book exists

    def test_retrieve_book(self):
        """ Test retrieving a single book by ID """
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_update_book(self):
        """ Test updating a book """
        data = {"title": "Updated Book"}
        response = self.client.patch(self.book_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Book")

    def test_delete_book(self):
        """ Test deleting a book """
        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_filter_books(self):
        """ Test filtering books by author """
        response = self.client.get(f"{self.list_url}?author=John Doe")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "John Doe")

    def test_search_books(self):
        """ Test searching books by title """
        response = self.client.get(f"{self.list_url}?search=Test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertIn("Test Book", response.data[0]["title"])

    def test_order_books(self):
        """ Test ordering books by publication year """
        Book.objects.create(title="Older Book", author="Alice", publication_year=2000)
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Older Book")  # First book should be the older one
