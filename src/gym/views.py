from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from gym.models import Actividades, Socios, Planes



def inicio (request):
    return render(request, "gym/index.html", {"mensaje": "Pagina de inicio"})

def actividades (request):
    actividades = Actividades.objects.all()
    return render(request, "gym/actividades.html", {"actividades": actividades})

def socios (request):
    socios = Socios.objects.all()
    return render(request, "gym/socios.html", {"socios": socios})

def planes (request):
    planes = Planes.objects.all()
    return render(request, "gym/planes.html", {"planes": planes})
    