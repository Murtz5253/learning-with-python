from django.shortcuts import get_object_or_404, render, redirect
from .models import Problem, ProblemForm, Solution, Topic

def home(request):
    return render(request, 'topics/home.html')

def topic(request):
    
    return render(request, 'topics/topic.html', {'title': 'List of Topics???'})

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
            solution.save()
            return redirect('/problems')
    else:
        form = ProblemForm(initial={'problem_code': problem.problem_code})
    return render(request, "topics/individual_problem.html", {
        "form": form
    })

def solutions(request):
    return render(request, "topics/solutions.html", {
        "solutions": Solution.objects.all()
    })