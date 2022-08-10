from django.shortcuts import render
from django.http import HttpResponse
from gym.models import Actividades, Socios, Planes
from gym.forms import *



def inicio (request):
    return render(request, "gym/index.html", {"mensaje": "Pagina de inicio"})

def actividades (request):
    actividades = Actividades.objects.all()

    if request.GET.get("nombre_actividad"):
        
        formulario_b = BusquedaActividades(request.GET)
        
        if formulario_b.is_valid():
            data = formulario_b.cleaned_data
            actividades = Actividades.objects.filter(nombre__icontains = data["nombre_actividad"])
        return render(request, "gym/actividades.html", {"actividades": actividades})
    
    else:
        formulario_b = BusquedaActividades()
        return render(request, "gym/actividades.html", {"actividades": actividades, "formulario": formulario_b})

def agregar_actividad(request):

    if request.method == "GET":
        formulario = AgregarActividades()
        return render(request, "gym/agregar_actividad.html", {"formulario": formulario})

    else:
        formulario = AgregarActividades(request.POST)

        if formulario.is_valid():
            
            data = formulario.cleaned_data
           
            nombre = data.get("nombre")
            dia = data.get("dia")
            horario = data.get("horario")
            cupo = data.get("cupo")
            
            actividad = Actividades(nombre=nombre, dia=dia, horario=horario, cupo=cupo)
            actividad.save()
            return render(request, "gym/index.html")

        else:
            return HttpResponse("Formulario no valido")

 
def socios (request):
    socios = Socios.objects.all()

    if request.GET.get("apellido_socio"):
        
        formulario_b = BusquedaSocios(request.GET)
        
        if formulario_b.is_valid():
            data = formulario_b.cleaned_data
            socios = Socios.objects.filter(apellido__icontains = data["apellido_socio"])
        return render(request, "gym/socios.html", {"socios": socios})
    
    else:
        formulario_b = BusquedaSocios()
        return render(request, "gym/socios.html", {"socios": socios, "formulario": formulario_b})

def agregar_socio(request):

    if request.method == "GET":
        formulario = AgregarSocios()
        return render(request, "gym/agregar_socio.html", {"formulario": formulario})

    else:
        formulario = AgregarSocios(request.POST)

        if formulario.is_valid():
            
            data = formulario.cleaned_data
           
            nombre = data.get("nombre")
            apellido = data.get("apellido")
            email= data.get("email")
            cuota_paga = data.get("cuota_paga")
            
            socio = Socios(nombre=nombre, apellido=apellido, email=email, cuota_paga=cuota_paga)
            socio.save()
            return render(request, "gym/index.html")

        else:
            return HttpResponse("Formulario no valido")


def planes (request):
    planes = Planes.objects.all()

    if request.GET.get("cantidad_clases_plan"):
    
        formulario_b = BusquedaPlanes(request.GET)
    
        if formulario_b.is_valid():
            data = formulario_b.cleaned_data
            planes = Planes.objects.filter(cantidad_clases__icontains = data["cantidad_clases_plan"])
        return render(request, "gym/planes.html", {"planes": planes})

    else:
        formulario_b = BusquedaPlanes()
        return render(request, "gym/planes.html", {"planes": planes, "formulario": formulario_b})
    
def agregar_plan(request):

    if request.method == "GET":
        formulario = AgregarPlanes()
        return render(request, "gym/agregar_plan.html", {"formulario": formulario})

    else:
        formulario = AgregarPlanes(request.POST)

        if formulario.is_valid():
            
            data = formulario.cleaned_data
           
            nombre = data.get("nombre")
            cantidad_clases = data.get("cantidad_clases")
            precio = data.get("precio")
            
            plan = Planes(nombre=nombre, cantidad_clases=cantidad_clases , precio=precio)
            plan.save()
            return render(request, "gym/index.html")

        else:
            return HttpResponse("Formulario no valido")