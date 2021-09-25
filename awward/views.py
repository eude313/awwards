from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from awward.models import Users
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from awward.models import *
# Create your views here.

def home(request):
    current_user = request.user
    profile_info = Profile.objects.filter(user=current_user).first()
    context = {'profile':profile_info}
    return render(request, 'awwards/home.html', context)

def register(request):
    if request.method == 'POST':
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        confirm_password= request.POST['confirm_password']
        if password == confirm_password:
            user = Users(username=username, email=email, password=make_password(password))
            user.save()
            messages.add_message(request, messages.SUCCESS, "Account created successfully!")
            return redirect('signIn')
    else:
        return render(request, 'auth/register.html')

def signIn(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Successfully logged in!")
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, "invalid infomation!") 
            return redirect("signIn") 
    else:
        return render(request, 'auth/signIn.html')

def signOut(request):
    logout(request)
    return redirect('signIn')

def profile(request):
    current_user = request.user
    if request.method == 'POST':
        image = request.FILES['image']
        bio = request.POST['bio']
        profile = Profile(user=current_user, image=image, bio=bio)
        profile.save()
        return redirect('profile')
    profile_info = Profile.objects.filter(user=current_user).first()
    context= {'profile':profile_info}   
    return render(request, 'awwards/profile.html', context)

def post(request):
    current_user = request.user
    if request.method == 'POST':
        title = request.POST['title']
        screen = request.FILES['image']
        description = request.POST['description']
        link = request.POST['link']
        post = Site(user=current_user, title=title, screen=screen, description=description, link=link)
        post.save()
        messages.add_message(request, messages.SUCCESS, "post created successfully")
        return redirect('home')
    else:
        post = Site.objects.all()
        context = {'posts': post}
        return render(request, 'awwards/post.html', context)