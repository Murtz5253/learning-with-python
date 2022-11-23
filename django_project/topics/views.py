from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, QuestionForm

def home(request):
    return render(request, 'topics/home.html')

def topic(request):
    return render(request, 'topics/topic.html', {'title': 'List of Topics'})

# def problems(request):
#     return render(request, 'topics/problems.html', {'title': 'List of Problems'})

def problems(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, initial={'question_code': '# YOUR CODE HERE'})
        if form.is_valid():
            form.save()
            return redirect('/problems')
    else:
        form = QuestionForm(initial={'question_code': '# YOUR CODE HERE'})
    return render(request, "topics/problems.html", {
        "form": form,
        "problems": Question.objects.all()
    })
