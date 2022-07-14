from django.urls import path
from .views import uetuni, ueuni, puuni, kcuni, ituuni, lcwuuni, gcuni
from . import views
urlpatterns = [
    path('gcuni/', gcuni, name="gcuni"),
    path('uetuni/', uetuni, name="uetuni"),
    path('ueuni/', ueuni, name="ueuni"),
    path('puuni/', puuni, name="puuni"),
    path('kcuni/', kcuni, name="kcuni"),
    path('lcwuuni/', lcwuuni, name="lcwuuni"),
]
   
