
from django.urls import path, include
from .views import UserRegistration, CustomAuthToken

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user-register'),
    path('login/', CustomAuthToken.as_view(), name='user-login'),
]