from django.shortcuts import render, redirect
from .models import Problem, ProblemForm, Solution

def home(request):
    return render(request, 'topics/home.html')

def topic(request):
    return render(request, 'topics/topic.html', {'title': 'List of Topics'})

def problems(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST, initial={'problem_code': '# YOUR CODE HERE'})
        if form.is_valid():
            # We want to store the user's response in a Solution DB object
            solution = Solution()
            solution.solution_code = form.cleaned_data['problem_code']
            solution.save()
            return redirect('/problems')
    else:
        form = ProblemForm(initial={'problem_code': '# YOUR CODE HERE'})
    return render(request, "topics/problems.html", {
        "form": form,
        "problems": Problem.objects.all()
    })

def solutions(request):
    return render(request, "topics/solutions.html", {
        "solutions": Solution.objects.all()
    })