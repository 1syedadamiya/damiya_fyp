from re import M
from django.db import models
from django.contrib.auth.models import User
 
class University (models.Model):
    department = models.CharField(max_length=50)
    merit_calculator = models.CharField(max_length=50)
    eligibilty_criteria = models.CharField(max_length=100)
    fee_structure = models.IntegerField()
    merit_list = models.IntegerField()
 
class Profile (models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    gender = (('F','Female'),('M','Male'))
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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
 
class Recommendation (models.Model):
    recommendationid = models.CharField(max_length=50)
 
class Feedback (models.Model):
    feedback_text = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
 
class Chatbot (models.Model):
    chat_history = models.CharField(max_length=100)
 
 

