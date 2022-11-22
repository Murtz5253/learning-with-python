from django.db import models
from django_ace import AceWidget
from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question, QuestionForm

class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm

admin.site.register(Question, QuestionAdmin)