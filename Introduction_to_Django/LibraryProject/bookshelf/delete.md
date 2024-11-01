# Delete Operation

Command:
```python
from bookshelf.models import Book  # Import the Book model

# Delete the book
retrieved_book.delete()

# Confirm deletion
all_books = Book.objects.all()
print(all_books)

