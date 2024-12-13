
from django.urls import path, include
from .views import UserRegistration, CustomAuthToken

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user-register'),
    path('login/', CustomAuthToken.as_view(), name='user-login'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]


