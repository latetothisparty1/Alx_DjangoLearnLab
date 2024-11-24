# api/views.py

from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all Book instances
    serializer_class = BookSerializer  # Use the BookSerializer to serialize the data

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieve all Book instances
    serializer_class = BookSerializer  # Use the BookSerializer to serialize the data
