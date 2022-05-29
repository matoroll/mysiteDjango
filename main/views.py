from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def articledetail(request):
    return render(request, 'article-details.html', {})


def privacypolicy(request):
    return render(request, 'privacy-policy.html', {})

def termsconditions(request):
    return render(request, 'terms-conditions.html', {})




def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.success(request, ("Złe dane wejściowe, spróbuj ponownie"))
            return redirect('log-in')

    else:
        return render(request, 'log-in.html',{})


def logout_user(request):
    logout(request)
    messages.success(request, ("Wylogowano"))
    return redirect('index')


def signup_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(email=email,username=username,password=password)
            login(request,user)
            messages.success(request, ("Pomyślnie zarejestrowano"))
            return redirect('index')
    else:
        form = RegisterUserForm()
    
    return render(request, 'sign-up.html', {
        'form':form,
    })
