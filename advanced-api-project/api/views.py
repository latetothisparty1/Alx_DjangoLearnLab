# api/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend, 
from django_filters import rest_framework
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    """
    View to list all books and create a new book.
    - GET: Retrieve a list of all books with filtering, searching, and ordering.
    - Filtering: Use query parameters like ?title=..., ?author=..., ?publication_year=...
    - Searching: Use ?search=... to search in title and author fields.
    - Ordering: Use ?ordering=... to order by title or publication_year.
    - POST: Create a new book (requires authentication).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ['title', 'author', 'publication_year']  # Fields to filter by
    search_fields = ['title', 'author']  # Fields to search in
    ordering_fields = ['title', 'publication_year']  # Fields to order by
    ordering = ['title']  # Default ordering

