from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def login_view(request):
    msg = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard")
        else:    
            msg = 'Invalid credentials'    
    else:
        msg = 'Error validating the form'    

    return render(request, "login.html", {"msg" : msg})

def register_user(request):
    msg     = None
    success = False

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        User.objects.create_user(username=username, password=password, email=email)
        msg     = 'User created.'
        success = True              
        return redirect('/login')
    else:
        msg = 'Form is not valid'

    return render(request, "register.html", {"msg" : msg, "success" : success })