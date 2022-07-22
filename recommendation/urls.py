from django.urls import path
from .views import dashboard, savedlinks
from . import views

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('savedlinks/', savedlinks, name="savedlinks"),
]

