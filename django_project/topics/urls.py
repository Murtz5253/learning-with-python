from django.urls import path
from . import views

urlpatterns = [
    # ex: /topics/
    path('', views.home, name='topics-home'),
    path('topic/', views.topic, name='topics-topic'),
    path('problems/', views.problems, name='topics-problems'),
    path('problems/<int:problem_id>/', views.problem_detail, name='topics-problem-detail'),
    path('solutions/', views.solutions, name='topics-solutions'),
    path('solutions/<int:problem_id>/', views.solution_detail, name='topics-solution-detail')
]
