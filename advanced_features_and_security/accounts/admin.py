from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser 

class CustomUser Admin(UserAdmin):
    model = CustomUser 
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser , CustomUser Admin)