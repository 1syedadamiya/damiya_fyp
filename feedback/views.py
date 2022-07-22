from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='login')
def feedback(request):
    return render(request, "feedback.html")
# Create your views here.
