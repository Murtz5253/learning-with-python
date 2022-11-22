from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'topics/home.html')

def topic(request):
    return render(request, 'topics/topic.html', {'title': 'List of Topics'})

def problems(request):
    return render(request, 'topics/problems.html', {'title': 'List of Problems'})