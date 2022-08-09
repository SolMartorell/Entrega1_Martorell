from django.urls import path
from gym.views import *

urlpatterns = [
    path('inicio/', inicio, name= "Inicio"),
    path("actividades/", actividades, name= "Actividades"),
    path("socios/", socios, name= "Socios"),
    path("planes/", planes, name= "Planes"),
]