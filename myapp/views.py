from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'myapp/home.html', {})

def about(request):
    return render(request, 'myapp/about.html', {})

def policy(request):
    return render(request, 'myapp/policy.html', {})

def refer_earn(request):
    return render(request, 'myapp/refer_earn.html', {})

def services(request):
    return render(request, 'myapp/services.html', {})

def contact(request):
    return render(request, 'myapp/contact.html', {})