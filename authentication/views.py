from django.contrib import auth
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from profiles.models import Profile


def login_view(request):
    msg = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # if not Profile.objects.filter['full_name']:
            #     return redirect("form")
            #     print("running")
            # else:
            #     print("not running")
            #     return redirect("/recommendation")
            return redirect("/recommendation")
        else:
            msg = 'Invalid credentials'


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
        return redirect('/form')
    else:
        msg = 'Form is not valid'

    return render(request, "register.html", {"msg" : msg, "success" : success })

class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect('home')

