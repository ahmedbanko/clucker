"""Configuration of admin interface for microbloges."""
from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Configuration of admin interface for users."""
    list_display = [
    'username', 'first_name', 'last_name', 'email', 'is_active',
    ]
