from django.shortcuts import render


def form(request):
    return render(request, "form.html")


def profile(request):
    return render(request, "profile.html")


def home(request):
    return render(request, "home.html")


def edit(request):
    return render(request, "edit.html")


