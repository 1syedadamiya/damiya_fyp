from django.shortcuts import render
from .models import University

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
  
def uetdepts(request,deptname):
    query = University.objects.filter(university_name__contains='University of Engineering and Technology') and University.objects.filter(program_abbreviation__contains=deptname)
    print(query)
    for value in query:
        program_name = value.program_name
        eligibilty_criteria = value.eligibilty_criteria
    context = {'program_name': program_name,
    'eligibilty_criteria': eligibilty_criteria
    }
    return render(request, "UETdepartments.html",context)

def uetuni(request):
    return render(request, "UETuni.html")
  
def ueuni(request):
    return render(request, "UEuni.html")

def gccs(request):
    return render(request, "GC[CS].html")

def gcee(request):
    return render(request, "GC[EE].html")

def itucs(request):
    return render(request, "ITU[CS].html")

def ituce(request):
    return render(request, "ITU[CE].html")

def ituee(request):
    return render(request, "ITU[EE].html")

def kccs(request):
    return render(request, "KC[CS].html")

def lcwuae(request):
    return render(request, "LCWU[AE].html")

def lcwucs(request):
    return render(request, "LCWU[CS].html")

def lcwucrp(request):
    return render(request, "LCWU[CRP].html")

def lcwuee(request):
    return render(request, "LCWU[EE].html")

def lcwuse(request):
    return render(request, "LCWU[SE].html")

def punewbbit(request):
    return render(request, "PUnew[BBIT].html")

def punewce(request):
    return render(request, "PUnew[CE].html")

def punewcs(request):
    return render(request, "PUnew[CS].html")

def punewds(request):
    return render(request, "PUnew[DS].html")

def punewit(request):
    return render(request, "PUnew[IT].html")

def punewee(request):
    return render(request, "PUnew[EE.html")

def punewiem(request):
    return render(request, "PUnew[IEM].html")

def punewenre(request):
    return render(request, "PUnew[Enr.E].html")

def punewmme(request):
    return render(request, "PUnew[MME].html")

def punewpe(request):
    return render(request, "PUnew[PE].html")

def punewse(request):
    return render(request, "PUnew[SE].html")

def punewte(request):
    return render(request, "PUnew[TE].html")


def puoldcs(request):
    return render(request, "PUold[CS].html")

def puoldds(request):
    return render(request, "PUold[DS].html")

def puoldit(request):
    return render(request, "PUold[IT].html")

def puoldse(request):
    return render(request, "PUold[SE].html")

def uecs(request):
    return render(request, "UE[CS].html")

def ueit(request):
    return render(request, "UE[IT].html")








