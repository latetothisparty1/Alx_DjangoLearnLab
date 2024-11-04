import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return None

# List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return None

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return Librarian.objects.get(library=library)
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Example usage
if __name__ == "__main__":
    author_books = books_by_author("J.K. Rowling")
    print(f"Books by J.K. Rowling: {[book.title for book in author_books]}")

    library_books = books_in_library("Central Library")
    print(f"Books in Central Library: {[book.title for book in library_books]}")

    librarian = librarian_for_library("Central Library")
    if librarian:
        print(f"Librarian for Central Library: {librarian.name}")
    else:
        print("No librarian found for Central Library.")