from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm



def signupview(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("pages:home")
        else:
            form = SignUpForm(request.POST)
            return render(request, "signup.html", {"form":form}) 
        
    else:
        form = SignUpForm()
        return render(request, "signup.html", {"form":form})


def loginview(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if (user is not None) and (user.is_active):
            login(request, user)
            return redirect("pages:home")
        else:
            form = AuthenticationForm(request.POST)
            return render(request, "login.html", {"form":form})        
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form":form})


def logoutview(request):
    return render(request, "logout.html")


def loggedoutview(request):
    logout(request)
    return redirect("accounts:login")

