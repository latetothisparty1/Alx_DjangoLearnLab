# relationship_app/admin.py
from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')  # Display user and role in the admin list view
    search_fields = ('user__username',)  # Allow searching by username

# Register the UserProfile model with the admin site
admin.site.register(UserProfile, UserProfileAdmin)