from django.contrib import admin
from .models import Book 

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Customize which fields to display
    search_fields = ('title', 'author__name')  # Enable searching by title and author's name
    list_filter = ('publication_year',)  # Enable filtering by publication year