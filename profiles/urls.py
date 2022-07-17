from django.urls import path
from .views import form, profile, home, dashboard, savedlinks
from . import views
urlpatterns = [
    path('form/', form, name="form"),
    path('profile/', profile, name="profile"),
    path('home/', home, name="home"),
    path('dashboard/', dashboard, name="dashboard"),
    path('savedlinks/', savedlinks, name="savedlinks"),
]
   
