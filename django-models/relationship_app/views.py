from django.shortcuts import render

# Create your views here.

# relationship_app/views.py
from django.views.generic import DetailView
from django.shortcuts import render
from .models import Book
from .models import Library

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# relationship_app/views.py




class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'