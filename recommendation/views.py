from django.shortcuts import render


def recommendation(request):
    return render(request, "recommendation.html")


def savedlinks(request):
    return render(request, "saved.html")
