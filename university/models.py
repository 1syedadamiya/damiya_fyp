from django.db import models
from django.contrib.auth.models import User
 
class University (models.Model):
    university_name = models.CharField(max_length=50)
    program_name = models.CharField(max_length=50)
    last_merit = models.IntegerField()
    eligibilty_criteria = models.CharField(max_length=500)
    fee_structure = models.IntegerField()
    
def __str__(self):
        return self.university_name
# Create your models here.
