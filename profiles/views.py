from django.shortcuts import render


def form(request):
    return render(request, "form.html")


def profile(request):
    return render(request, "profile.html")


def home(request):
    return render(request, "home.html")


def dashboard(request):
    return render(request, "recommendation.html")

def savedlinks(request):
    return render(request, "saved.html")
