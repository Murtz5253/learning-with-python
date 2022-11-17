from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='topics-home'),
    path('topic/', views.topic, name='topics-topic'),
]