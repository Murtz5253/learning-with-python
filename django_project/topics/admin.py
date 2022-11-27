from django.db import models
from django_ace import AceWidget
from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Problem, ProblemForm, Solution

class ProblemAdmin(admin.ModelAdmin):
    form = ProblemForm

class SolutionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Solution, SolutionAdmin)