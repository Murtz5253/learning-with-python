"""This module generates the topic application"""

from django.apps import AppConfig


class TopicsConfig(AppConfig):
    """Creates field to add topics"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'topics'
