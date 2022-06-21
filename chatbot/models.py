from django.db import models

 
class Chatbot (models.Model):
    chat_history = models.CharField(max_length=100)
# Create your models here.
