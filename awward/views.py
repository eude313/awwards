from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'awwards/home.html')

def register(request):
    return render(request, 'auth/register.html')

def signIn(request):
    return render(request, 'auth/signIn.html')
