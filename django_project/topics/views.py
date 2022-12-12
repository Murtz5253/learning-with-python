"""This module renders the views for the website"""

from django.shortcuts import get_object_or_404, render, redirect
from .models import Problem, ProblemForm, Solution, SolutionForm

def home(request):
    """Renders home page"""
    return render(request, 'topics/home.html')

def topic(request):
    """Renders topic list page"""
    return render(request, 'topics/topic.html', {'title': 'List of Topics'})

def topic1(request):
    """Renders topic 1 page"""
    return render(request, 'topics/topic1.html',
                  {'title': 'Topic 1: Function Parameter Use and Scope'})

def topic2(request):
    """Renders topic 2 page"""
    return render(request, 'topics/topic2.html',
                  {'title': 'Topic 2: Variables, Identifiers, and Scope'})

def topic3(request):
    """Renders topic 3 page"""
    return render(request, 'topics/topic3.html', {'title': 'Topic 3: Recursion'})

def topic4(request):
    """Renders topic 4 page"""
    return render(request, 'topics/topic4.html', {'title': 'Topic 4: Iteration'})

def topic5(request):
    """Renders topic 5 page"""
    return render(request, 'topics/topic5.html', {'title': 'Topic 5: Objects'})

def topic6(request):
    """Renders topic 6 page"""
    return render(request, 'topics/topic6.html', {'title': 'Boolean Expressions'})

def problems(request):
    """Renders proplem list page"""
    problem_list = Problem.objects.order_by('problem_id')
    problem_dict = {'1': list(), '2': list(), '3': list(), '4': list(), '5': list(), '6': list()}
    for problem in problem_list:
        problem_dict[str(problem.topic_number)].append(problem)
    context = {'problem_dict': problem_dict}
    return render(request, 'topics/problems.html', context)

def problem_detail(request, problem_id):
    """Renders individual problem page"""
    problem = get_object_or_404(Problem, pk=problem_id)
    if request.method == 'POST':
        form = ProblemForm(request.POST, initial={'problem_code': problem.problem_code})
        if form.is_valid():
            # We want to store the user's response in a Solution DB object
            solution = Solution()
            solution.solution_code = form.cleaned_data['problem_code']
            solution.problem = problem
            solution.user = request.user
            solution.save()
            return redirect('/problems')
    else:
        form = ProblemForm(initial={'problem_code': problem.problem_code})
    return render(request, "topics/individual_problem.html", {
        "form": form
    })

def solutions(request):
    """Renders list of all submitted solutions page"""
    problem_list = Problem.objects.order_by('problem_id')
    context = {'problem_list': problem_list}
    return render(request, 'topics/solutions.html', context)

def solution_detail(request, problem_id):
    """Renders individual solutions"""
    problem = get_object_or_404(Problem, pk=problem_id)
    # one_solution = problem.solutions.all()[0]
    # form = SolutionForm(initial={'solution_code': one_solution.solution_code})
    # return render(request, "topics/solutions_by_problem.html", {
    #     "form": form
    # })
    forms = list()
    for solution in problem.solutions.all():
        if solution.user == request.user:
            # We only want to display the solutions for the current user
            forms.append(SolutionForm(initial={'solution_code': solution.solution_code}))
    return render(request, "topics/solutions_by_problem.html", {
        'forms': forms
    })

def test(request):
    """
    Renders view progress page. This is currently hardcoded
    for the 4 example student use cases according to our data,
    but will eventually be updated to show the data of actual
    student that register and are saved into the database.

    For any user that is not one of the four example students, it currently
    just defaults to Student 4's data.
    """
    if request.user.username == 'student1':
        return render(request, 'topics/student1_progress.html', {'title': 'View Progress'})
    elif request.user.username == 'student2':
        return render(request, 'topics/student2_progress.html', {'title': 'View Progress'})
    elif request.user.username == 'student3':
        return render(request, 'topics/student3_progress.html', {'title': 'View Progress'})
    else:
        return render(request, 'topics/student4_progress.html', {'title': 'View Progress'})
