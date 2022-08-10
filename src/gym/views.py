from django.shortcuts import render
from django.http import HttpResponse
from gym.models import Actividades, Socios, Planes
from gym.forms import BusquedaActividades, BusquedaSocios, BusquedaPlanes




def inicio (request):
    return render(request, "gym/index.html", {"mensaje": "Pagina de inicio"})

def actividades (request):
    actividades = Actividades.objects.all()

    if request.GET.get("nombre_actividad"):
        
        formulario = BusquedaActividades(request.GET)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            actividades = Actividades.objects.filter(nombre__icontains = data["nombre_actividad"])
        return render(request, "gym/actividades.html", {"actividades": actividades})
    
    else:
        formulario = BusquedaActividades()
        return render(request, "gym/actividades.html", {"actividades": actividades, "formulario": formulario})



    
def socios (request):
    socios = Socios.objects.all()

    if request.GET.get("apellido_socio"):
        
        formulario = BusquedaSocios(request.GET)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            socios = Socios.objects.filter(apellido__icontains = data["apellido_socio"])
        return render(request, "gym/socios.html", {"socios": socios})
    
    else:
        formulario = BusquedaSocios()
        return render(request, "gym/socios.html", {"socios": socios, "formulario": formulario})



def planes (request):
    planes = Planes.objects.all()

    if request.GET.get("cantidad_clases_plan"):
    
        formulario = BusquedaPlanes(request.GET)
    
        if formulario.is_valid():
            data = formulario.cleaned_data
            planes = Planes.objects.filter(cantidad_clases__icontains = data["cantidad_clases_plan"])
        return render(request, "gym/planes.html", {"planes": planes})

    else:
        formulario = BusquedaPlanes()
        return render(request, "gym/planes.html", {"planes": planes, "formulario": formulario})
    
    