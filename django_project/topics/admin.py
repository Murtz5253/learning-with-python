"""Administration site setup"""

#from django.db import models
from django_ace import AceWidget
from django.contrib import admin
from .models import Problem, ProblemForm, Solution, SolutionForm

# Register your models here.

class ProblemAdmin(admin.ModelAdmin):
    """Creates the problem set database"""
    form = ProblemForm

class SolutionAdmin(admin.ModelAdmin):
    """Creates the solution set database"""
    form = SolutionForm

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Solution, SolutionAdmin)
