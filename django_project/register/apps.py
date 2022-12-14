"""This module configures the register form"""
from django.apps import AppConfig


class RegisterConfig(AppConfig):
    """Sets registration configuration to autofield and name register"""
    default_auto_field = "django.db.models.BigAutoField"
    name = "register"
