"""This module creates the user admin page"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """This class creates a custom user admin"""
    form = RegisterForm
    model = CustomUser
    list_display = ["username", "email", "password"]

admin.site.register(CustomUser, CustomUserAdmin)
