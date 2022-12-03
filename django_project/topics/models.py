from django.db import models
from django import forms
from django.forms import ModelForm
from django_ace import AceWidget
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Problem(models.Model):
    """
    This class represents a practice question for the web application.
    It will be stored as a multi-line string with indents, and
    displayed inside of a code editor.
    """
    problem_id = models.IntegerField(primary_key=True, default=-1)
    problem_code = models.TextField(default="")

class ProblemForm(ModelForm):
    """
    This ModelForm is an adjunct to the Problem class to allow usage
    of the Ace Widget Code Editor as well as provide a place for the
    user to submit code. Its only field is the same field as the
    Problem class, storing the skeleton code as formatted text.
    """
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
    # Will need to eventually add foreign key to reference student/user
    # student = ...

    # Define a relationship to the associated problem for this solution
    # The "related_name" parameter will let us access all of a problem's solutions
    # To do so, use the syntax "problem.solutions.all()"
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="solutions")

    # Store the solution code
    solution_code = models.TextField(default="")

class SolutionForm(ModelForm):
    """
    This ModelForm is an adjunct to the Solution class.
    Technically, a form is not necessary for Solutions.
    However, this is a workaround so that the AceWidget
    can be used to format the code properly. The submit
    button will be hidden, so this will not function like
    a traditional form.
    """
    class Meta:
        model = Solution
        fields = ['solution_code']
        widgets = {
            'solution_code': AceWidget(mode='python', theme='twilight'),
        }
