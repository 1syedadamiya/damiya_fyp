from django.shortcuts import render

def gcuni(request):
    return render(request, "GCuni.html")
  
def ituuni(request):
    return render(request, "ITUuni.html")
  
def puuni(request):
    return render(request, "PUuni.html")

def kcuni(request):
    return render(request, "KCuni.html")
  
def lcwuuni(request):
    return render(request, "LCWUuni.html")
  
def uetuni(request):
    return render(request, "UETuni.html")
  
def ueuni(request):
    return render(request, "UEuni.html")
