# blog/urls.py
from django.urls import path
from .views import register, user_login, user_logout, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
]

["post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/"]
