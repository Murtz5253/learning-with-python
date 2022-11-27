from django.db import models
from django import forms
from django.forms import ModelForm
from django_ace import AceWidget

# Create your models here.
class Problem(models.Model):
    """
    This class represents a practice question for the web application.
    It will be stored as a multi-line string with indents, and
    displayed inside of a code editor.
    """
    problem_code = models.TextField(default="")

class ProblemForm(ModelForm):
    class Meta:
        model = Problem
        fields = ['problem_code']
        widgets = {
            'problem_code': AceWidget(mode='python', theme='twilight'),
        }
    
class Solution(models.Model):
    """
    This class represents the submitted solution.
    It will be stored as a multi-line string with indents.
    """
    # Will need to eventually add foreign key or reference to Question + student_id
    # question_object, student_id =

    # Store the solution code
    solution_code = models.TextField(default="")