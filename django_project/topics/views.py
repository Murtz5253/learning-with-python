from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import QuestionForm

def home(request):
    return render(request, 'topics/home.html')

def topic(request):
    return render(request, 'topics/topic.html', {'title': 'List of Topics'})

# def problems(request):
#     return render(request, 'topics/problems.html', {'title': 'List of Problems'})

def problems(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QuestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuestionForm()
    return render(request, 'topics/problems.html', {'title': 'List of Problems', 'form': form})
