"""This module creates the cusom user model"""
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    """This class creates the custom user model"""
    #pass
    # add additional fields in here
    # uncomment pass when you want to add additional fields

    def __str__(self):
        """Creates a username"""
        return self.username
