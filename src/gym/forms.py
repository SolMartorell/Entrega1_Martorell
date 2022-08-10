from django.forms import Form, CharField, IntegerField, EmailField, BooleanField

class BusquedaActividades(Form):
    nombre_actividad = CharField(max_length=30)

class BusquedaSocios(Form):
    apellido_socio = CharField(max_length=30)

class BusquedaPlanes(Form):
    cantidad_clases_plan = IntegerField()
