from django.forms import Form, CharField, IntegerField, EmailField, BooleanField

class BusquedaActividades(Form):
    nombre_actividad = CharField(max_length=30)

class BusquedaSocios(Form):
    apellido_socio = CharField(max_length=30)

class BusquedaPlanes(Form):
    cantidad_clases_plan = IntegerField()



class AgregarActividades(Form):
    nombre = CharField(max_length=30)
    dia = CharField(max_length=30)
    horario = IntegerField()
    cupo = IntegerField()

class AgregarSocios(Form):
    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30)
    email = EmailField()
    cuota_paga = BooleanField()

class AgregarPlanes(Form):
    nombre = CharField(max_length=30)
    cantidad_clases = IntegerField()
    precio = IntegerField()