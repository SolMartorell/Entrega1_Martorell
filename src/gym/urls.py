from django.urls import path
from gym.views import *

urlpatterns = [
    path('inicio/', inicio, name= "Inicio"),
    path("actividades/", actividades, name= "Actividades"),
    path("socios/", socios, name= "Socios"),
    path("planes/", planes, name= "Planes"),
    path("actividades/agregar", agregar_actividad, name= "Agregar Actividad"),
    path("socios/agregar", agregar_socio, name= "Agregar Socio"),
    path("planes/agregar", agregar_plan, name= "Agregar Plan"),
]