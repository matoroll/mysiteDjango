from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def articledetail(request):
    return render(request, 'article-details.html', {})

def login(request):
    return render(request, 'log-in.html', {})

def privacypolicy(request):
    return render(request, 'privacy-policy.html', {})

def signup(request):
    return render(request, 'sign-up.html', {})

def termsconditions(request):
    return render(request, 'terms-conditions.html', {})


