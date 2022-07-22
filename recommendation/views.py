from django.shortcuts import render


def dashboard(request):
    return render(request, "recommendation.html")


def savedlinks(request):
    return render(request, "saved.html")
