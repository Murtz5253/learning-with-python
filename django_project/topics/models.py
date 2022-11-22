from django.db import models
from django import forms
from django.forms import ModelForm
from django_ace import AceWidget

# Create your models here.
class Question(models.Model):
    """
    This class represents a practice question for the web application.
    It will be stored as a multi-line string with indents, and
    displayed inside of a code editor.
    """
    question_code = models.TextField(default="")

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_code']
        widgets = {
            'question_code': AceWidget,
        }