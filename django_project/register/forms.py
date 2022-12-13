"""This module creates the registration form"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):
    """This class creates a registration form object"""
    email = forms.EmailField()

    class Meta:
        """This class specifies the fields for the registration form"""
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]
