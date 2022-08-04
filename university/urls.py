from django.urls import path
from .views import uetuni, ueuni, puuni, kcuni, ituuni, lcwuuni, gcuni, gcdepts, itudepts, kcdepts, lcwudepts, pudepts, uetdepts, uedepts
from . import views
urlpatterns = [
    path('gcuni/', gcuni, name="gcuni"),
    path('gcuni/<str:deptname>/', gcdepts, name="gcdepts"),
    path('uetuni/', uetuni, name="uetuni"),
    path('uetuni/<str:deptname>/', uetdepts, name="uetdepts"),
    path('ueuni/', ueuni, name="ueuni"),
    path('ueuni/<str:deptname>/', uedepts, name="uedepts"),
    path('puuni/', puuni, name="puuni"),
    path('puuni/<str:deptname>/', pudepts, name="pudepts"),
    # path('puuni/<str:deptname>/', puodepts, name="puodepts"),
    path('kcuni/', kcuni, name="kcuni"),
    path('kcuni/<str:deptname>/', kcdepts, name="kcdepts"),
    path('lcwuuni/', lcwuuni, name="lcwuuni"),
    path('lcwuuni/<str:deptname>/', lcwudepts, name="lcwudepts"),
    path('ituuni/', ituuni, name="ituuni"),
    path('ituuni/<str:deptname>/', itudepts, name="itudepts"),
]
   
