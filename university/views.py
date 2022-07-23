from django.shortcuts import render
from .models import University

def gcuni(request):
    return render(request, "GCuni.html")

def gcdepts(request,deptname):
    query = University.objects.filter(university_name__contains='Government College University Lahore') and University.objects.filter(program_abbreviation__contains=deptname)
    print(query)
    for value in query:
        program_name = value.program_name
        eligibilty_criteria = value.eligibilty_criteria
        fee_structure = value.fee_structure
        last_merit = value.last_merit
    context = {'program_name': program_name,
    'eligibilty_criteria': eligibilty_criteria,
    'fee_structure': fee_structure,
    'last_merit': last_merit,
    }
    return render(request, "GCdepartments.html",context)
  
def ituuni(request):
    return render(request, "ITUuni.html")

def itudepts(request,deptname):
    query = University.objects.filter(university_name__contains='Information Technology University') and University.objects.filter(program_abbreviation__contains=deptname)
    print(query)
    for value in query:
        program_name = value.program_name
        eligibilty_criteria = value.eligibilty_criteria
        fee_structure = value.fee_structure
        last_merit = value.last_merit
    context = {'program_name': program_name,
    'eligibilty_criteria': eligibilty_criteria,
    'fee_structure': fee_structure,
    'last_merit': last_merit,
    }
    return render(request, "ITUdepartments.html",context)
  
def puuni(request):
    return render(request, "PUuni.html")

def pundepts(request,deptname):
    query = University.objects.filter(university_name__contains='Punjab University') and University.objects.filter(program_abbreviation__contains=deptname)
    print(query)
    for value in query:
        program_name = value.program_name
        eligibilty_criteria = value.eligibilty_criteria
        fee_structure = value.fee_structure
        last_merit = value.last_merit
    context = {'program_name': program_name,
    'eligibilty_criteria': eligibilty_criteria,
    'fee_structure': fee_structure,
    'last_merit': last_merit,
    }
    return render(request, "PUnewdepartments.html",context)

def puodepts(request,deptname):
    query = University.objects.filter(university_name__contains='Punjab University') and University.objects.filter(program_abbreviation__contains=deptname)
    print(query)
    for value in query:
        program_name = value.program_name
        eligibilty_criteria = value.eligibilty_criteria
        fee_structure = value.fee_structure
        last_merit = value.last_merit
    context = {'program_name': program_name,
    'eligibilty_criteria': eligibilty_criteria,
    'fee_structure': fee_structure,
    'last_merit': last_merit,
    }
    return render(request, "PUolddepartments.html",context)

def kcuni(request):
    return render(request, "KCuni.html")

def kcdepts(request,deptname):
    query = University.objects.filter(university_name__contains='Kinnard College For Women University') and University.objects.filter(program_abbreviation__contains=deptname)
    print(query)
    print(deptname)
    for value in query:
        program_name = value.program_name
        eligibilty_criteria = value.eligibilty_criteria
        fee_structure = value.fee_structure
        last_merit = value.last_merit
        print(last_merit)
    context = {'program_name': program_name,
    'eligibilty_criteria': eligibilty_criteria,
    'fee_structure': fee_structure,
    'last_merit': last_merit,
    }
    return render(request, "KCdepartments.html",context)
  
def lcwuuni(request):
    return render(request, "LCWUuni.html")

def lcwudepts(request,deptname):
    query = University.objects.filter(university_name__contains='Lahore College for Women University') and University.objects.filter(program_abbreviation__contains=deptname)
    print(query)
    for value in query:
        program_name = value.program_name
        eligibilty_criteria = value.eligibilty_criteria
        fee_structure = value.fee_structure
        last_merit = value.last_merit
    context = {'program_name': program_name,
    'eligibilty_criteria': eligibilty_criteria,
    'fee_structure': fee_structure,
    'last_merit': last_merit,
    }
    return render(request, "LCWUdepartments.html",context)

def uetuni(request):
    return render(request, "UETuni.html")

def uetdepts(request,deptname):
    query = University.objects.filter(university_name__contains='University of Engineering and Technology') and University.objects.filter(program_abbreviation__contains=deptname)
    print(query)
    for value in query:
        program_name = value.program_name
        eligibilty_criteria = value.eligibilty_criteria
        fee_structure = value.fee_structure
        last_merit = value.last_merit
    context = {'program_name': program_name,
    'eligibilty_criteria': eligibilty_criteria
    }
    return render(request, "UETdepartments.html",context)
  
def ueuni(request):
    return render(request, "UEuni.html")

def uedepts(request,deptname):
    query = University.objects.filter(university_name__contains='University of Education') and University.objects.filter(program_abbreviation__contains=deptname)
    print(query)
    for value in query:
        program_name = value.program_name
        eligibilty_criteria = value.eligibilty_criteria
        fee_structure = value.fee_structure
        last_merit = value.last_merit
    context = {'program_name': program_name,
    'eligibilty_criteria': eligibilty_criteria,
    'fee_structure': fee_structure,
    'last_merit': last_merit,
    }
    return render(request, "UEdepartments.html",context)
