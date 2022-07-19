from django.db import models
from django.contrib.auth.models import User
 
class University (models.Model):
    university_name = models.CharField(max_length=50)
    program_name = models.CharField(max_length=50)
    last_merit = models.IntegerField()
    eligibilty_criteria = models.CharField(max_length=100)
    fee_structure = models.IntegerField()
    

# Create your models here.
