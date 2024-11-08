# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView, user_login, user_logout, user_register
from .views import (
    list_books,
    add_book,
    delete_book,
    LibraryDetailView,
    user_login,
    user_logout,
    user_register,
    admin_view, 
    librarian_view, 
    member_view,
)

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('books/add/', add_book, name='add_book'),  # URL for adding a book
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),  # URL for editing a book
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),  # URL for deleting a book
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]

add_book/", "edit_book/
