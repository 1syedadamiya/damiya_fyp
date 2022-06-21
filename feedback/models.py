from django.db import models
from django.contrib.auth.models import User

class Feedback (models.Model):
    feedback_text = models.CharField(max_length=100)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
# Create your models here.
