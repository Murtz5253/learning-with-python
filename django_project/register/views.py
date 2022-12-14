"""Renders webpage for registration site"""
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import Http404
from .forms import RegisterForm


# Create your views here.
def register(response):
    """Creating registration webpage"""
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            print("VALID")
            User = get_user_model()
            User.objects.create_user(username=form.cleaned_data['username'],
                                     email=form.cleaned_data['email'],
                                     password=form.cleaned_data['password1'])
        else:
            print("INVALID")
            print(form.errors)
            raise Http404
        return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})
