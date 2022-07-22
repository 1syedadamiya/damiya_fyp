from django.urls import path
from .views import form, profile, home
from . import views
urlpatterns = [
    path('form/', form, name="form"),
    path('profile/', profile, name="profile"),
    path('home/', home, name="home"),
]
   
