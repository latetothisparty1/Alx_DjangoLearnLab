# my_project/urls.py

from django.contrib import admin
from django.urls import path, include  # Make sure to import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),  # Include the app's URLs
]