from django.http import HttpResponseRedirect
from django.shortcuts import render
from university.models import SavedItems,University,UniversitiesCount
from profiles.models import Profile

def recommendation(request):
    profile = Profile.objects.get(student=request.user)
    matric_marks = profile.matric_marks
    matric_grade = profile.matric_grade
    inter_marks = profile.inter_marks
    inter_grade = profile.inter_grade
    university_name = profile.university_name
    field_of_interest = profile.field_of_interest
    matric_marks_percentange = (matric_marks/1100)*30
    inter_marks_percentange = (inter_marks/1100)*70
    final_percentange = matric_marks_percentange + inter_marks_percentange
    query = University.objects.filter(program_abbreviation="CS",last_merit__lte=final_percentange)
    query2 = UniversitiesCount.objects.order_by('-count')[:5]
    return render(request, "recommendation.html",context={'final_query':query,'final_query2':query2})


def savedlinks(request):
    query = SavedItems.objects.filter(user=request.user)
    # if request.method == 'POST':
    #     query.delete()
    #     return HttpResponseRedirect ("/")
    return render(request, "saved.html",context={'query':query})


def aboutus(request):
    return render(request, "aboutus.html")
