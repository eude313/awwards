from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'awwards/home.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user = 
        
    else:
        return render(request, 'auth/register.html')

def signIn(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
    else:
        return render(request, 'auth/signIn.html')
