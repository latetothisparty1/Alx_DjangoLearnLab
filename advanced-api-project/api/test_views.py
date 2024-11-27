import json
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from .models import Book
from .serializers import BookSerializer

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'publication_year': 2023
        }

    def test_create_book(self):
        response = self.client.post('/api/books/', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)

    def test_retrieve_book(self):
        book = Book.objects.create(**self.book_data)
        response = self.client.get(f'/api/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, BookSerializer(book).data)

    def test_update_book(self):
        book = Book.objects.create(**self.book_data)
        updated_data = {'title': 'Updated Test Book'}
        response = self.client.put(f'/api/books/{book.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(id=book.id).title, updated_data['title'])

    def test_delete_book(self):
        book = Book.objects.create(**self.book_data)
        response = self.client.delete(f'/api/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filtering(self):
        book1 = Book.objects.create(title='Test Book 1', author='Test Author 1', publication_year=2022)
        book2 = Book.objects.create(title='Test Book 2', author='Test Author 2', publication_year=2023)
        response = self.client.get('/api/books/?publication_year=2023')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], book2.title)

    def test_searching(self):
        book1 = Book.objects.create(title='Test Book 1', author='Test Author 1', publication_year=2022)
        book2 = Book.objects.create(title='Test Book 2', author='Test Author 2', publication_year=2023)
        response = self.client.get('/api/books/?search=Test Book 2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], book2.title)

    def test_ordering(self):
        book1 = Book.objects.create(title='Test Book 1', author='Test Author 1', publication_year=2022)
        book2 = Book.objects.create(title='Test Book 2', author='Test Author 2', publication_year=2023)
        response = self.client.get('/api/books/?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], book1.title)
        self.assertEqual(response.data[1]['title'], book2.title)

self.client.login