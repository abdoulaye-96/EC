from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserRegisterForm
from .models import *


def home(request):
    return render(request, 'home.html')

def login_page(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/user/home/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})

def logout_page(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return render(request, 'logout.html')

def register_page(request):
    """Register a new user"""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
            messages.success(request, "Registration successful. You can now log in.")
            return render(request, 'home.html', {'form': form})
        else:
            messages.error(request, "Registration failed. Please try again.")
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
