from django.db import models
from django.contrib.auth.models import User


class Feedback (models.Model):
   name = models.CharField(max_length=50)
   email = models.EmailField()
   Feedback_text = models.CharField(max_length=1000)

   def _str_(self):
       return str(self.name)
