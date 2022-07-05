from django.urls import path
from .views import form, profile
from . import views
urlpatterns = [
    path('form/', form, name="form"),
    path('profile/', profile, name="profile"),
]
   
