from django.shortcuts import get_object_or_404, render, redirect
from .models import Problem, ProblemForm, Solution, SolutionForm

def home(request):
    return render(request, 'topics/home.html')

def topic(request):
    return render(request, 'topics/topic.html', {'title': 'List of Topics'})

def topic1(request):
    return render(request, 'topics/topic1.html', {'title': 'Topic 1: Function Parameter Use and Scope'})

def topic2(request):
    return render(request, 'topics/topic2.html', {'title': 'Topic 2: Variables, Identifiers, and Scope'})

def topic3(request):
    return render(request, 'topics/topic3.html', {'title': 'Topic 3: Recursion'})

def topic4(request):
    return render(request, 'topics/topic4.html', {'title': 'Topic 4: Iteration'})

def topic5(request):
    return render(request, 'topics/topic5.html', {'title': 'Topic 5: Objects'})

def topic6(request):
    return render(request, 'topics/topic6.html', {'title': 'Boolean Expressions'})

def problems(request):
    problem_list = Problem.objects.order_by('problem_id')
    context = {'problem_list': problem_list}
    return render(request, 'topics/problems.html', context)

def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    if request.method == 'POST':
        form = ProblemForm(request.POST, initial={'problem_code': problem.problem_code})
        if form.is_valid():
            # We want to store the user's response in a Solution DB object
            solution = Solution()
            solution.solution_code = form.cleaned_data['problem_code']
            solution.problem = problem
            solution.save()
            return redirect('/problems')
    else:
        form = ProblemForm(initial={'problem_code': problem.problem_code})
    return render(request, "topics/individual_problem.html", {
        "form": form
    })

def solutions(request):
    problem_list = Problem.objects.order_by('problem_id')
    context = {'problem_list': problem_list}
    return render(request, 'topics/solutions.html', context)

def solution_detail(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    # one_solution = problem.solutions.all()[0]
    # form = SolutionForm(initial={'solution_code': one_solution.solution_code})
    # return render(request, "topics/solutions_by_problem.html", {
    #     "form": form
    # })
    forms = list()
    for solution in problem.solutions.all():
        forms.append(SolutionForm(initial={'solution_code': solution.solution_code}))
    return render(request, "topics/solutions_by_problem.html", {
        'forms': forms
    })