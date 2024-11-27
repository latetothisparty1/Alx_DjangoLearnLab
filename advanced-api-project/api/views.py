# api/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    """
    View to list all books and create a new book.
    - GET: Retrieve a list of all books.
    - POST: Create a new book (requires authentication).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access to unauthenticated users

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a book by ID.
    - GET: Retrieve a book by its ID.
    - PUT: Update a book by its ID (requires authentication).
    - DELETE: Delete a book by its ID (requires authentication).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access to unauthenticated users