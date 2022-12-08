"""This module generates the urls for the webpage"""
"""This is a Django generated module"""
from django.urls import path
from . import views

urlpatterns = [
    # ex: /topics/
    path('', views.home, name='topics-home'),
    path('topic/', views.topic, name='topics-topic'),
    path('topic1/', views.topic1, name='topics-topic1'),
    path('topic2/', views.topic2, name='topics-topic2'),
    path('topic3/', views.topic3, name='topics-topic3'),
    path('topic4/', views.topic4, name='topics-topic4'),
    path('topic5/', views.topic5, name='topics-topic5'),
    path('topic6/', views.topic6, name='topics-topic6'),
    path('problems/', views.problems, name='topics-problems'),
    path('problems/<int:problem_id>/', views.problem_detail, name='topics-problem-detail'),
    path('solutions/', views.solutions, name='topics-solutions'),
    path('solutions/<int:problem_id>/', views.solution_detail, name='topics-solution-detail'),
    path('progress/', views.progress, name='topics-test')
]
