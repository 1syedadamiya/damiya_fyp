from django.db import models
from django.contrib.auth.models import User

 
choices = (('F','Female'),('M','Male'))
class Profile(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=15,choices=choices,default="Male")
    age = models.IntegerField()
    religion = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    gaurdian_name = models.CharField(max_length=50)
    gaurdian_income = models.IntegerField()
    name_of_school = models.CharField(max_length=50)
    matric_marks = models.IntegerField()
    year_of_matric = models.IntegerField()
    matric_grade = models.CharField(max_length=10)
    matric_board = models.CharField(max_length=50)
    name_of_college = models.CharField(max_length=50)
    inter_marks = models.IntegerField()
    year_of_inter = models.IntegerField()
    inter_grade = models.CharField(max_length=10)
    inter_board = models.CharField(max_length=50)
    university_name = models.CharField(max_length=50)
    field_of_interest = models.CharField(max_length=50)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student)
# Create your models here.
