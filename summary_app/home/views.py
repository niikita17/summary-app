from django.shortcuts import render

# Create your views here.
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from django.contrib.auth import logout
# Create your views here.
# from .models import Note
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def Home(request):
    return render(request,'home/main.html',{})



def registration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        fname =request.POST.get('fname')
        lname =request.POST.get('lname')
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if username and password and email and fname and lname:
            
            try:
                user = User.objects.create_user(username=username,first_name=fname, last_name=lname, email=email, password=password)
                
                login(request,user)  # Log the user in after registration
                return redirect("login_user")
                
            except IntegrityError:  # Handle case where username or email is not unique
                return HttpResponse("Username or email is already taken")
    return render(request, "home/signup.html", {})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if password and username:
            user = authenticate(request, username=username, password= password)
            if user is not None:
                login(request,user)
                return redirect('Home')
            else:
                return HttpResponse("Invalid credentials")
    return render(request, "home/login.html", {})





        
    





def logout_view(request):
    logout(request)
    return render(request,'home/main.html',{})
    