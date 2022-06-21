#from django.contrib import admin
#from .models import University, Recommendation, Profile, Feedback, Chatbot

#admin.site.register(University)
#admin.site.register(Recommendation)
#admin.site.register(Profile)
#admin.site.register(Feedback)
#admin.site.register(Chatbot)


# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.

admin.site.unregister(Group)