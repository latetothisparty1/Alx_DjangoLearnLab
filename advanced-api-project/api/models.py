# api/models.py

from django.db import models

class Author(models.Model):
    """
    Model representing an author.
    """
    name = models.CharField(max_length=100)  # Author's name

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model representing a book.
    """
    title = models.CharField(max_length=200)  # Book's title
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # Link to Author

    def __str__(self):
        return self.title