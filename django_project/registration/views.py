# views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect("/home")
    else:
        form = RegistrationForm()

    return render(response, "registration/registration.html", {"form":form})
