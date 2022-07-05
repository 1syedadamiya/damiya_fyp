from django.urls import path
from .views import form
from . import views
urlpatterns = [
    path('form/', form, name="form"),
]
   
