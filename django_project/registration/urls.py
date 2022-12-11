"""This module generates the urls for the webpage"""

from django.urls import path
from . import views

app_name = 'registration'
urlpatterns = [
    # ex: /topics/
    path('', views.register, name='register')
]
