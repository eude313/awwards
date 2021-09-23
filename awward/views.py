from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, 'awwards/home.html')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signIn')
    context = {'form': form}
    return render(request, 'auth/register.html', context)

def signIn(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
    else:
        return render(request, 'auth/signIn.html')
