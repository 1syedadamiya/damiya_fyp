from django.db import models
from django.contrib.auth.models import User
 
class University (models.Model):
    department = models.CharField(max_length=50)
    merit_calculator = models.CharField(max_length=50)
    eligibilty_criteria = models.CharField(max_length=100)
    fee_structure = models.IntegerField()
    merit_list = models.IntegerField()

# Create your models here.
