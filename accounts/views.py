from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'accounts/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        age = request.POST['age']

        user = User.objects.create_user(username = username, password = password, email = email)
        user.save()
        return redirect('login')
    return render(request, 'accounts/register.html')

def home_view(request):
    return render(request, 'accounts/home.html')

def landing_vew(request):
    return render(request, 'accounts/landing.html')