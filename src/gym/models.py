from django.db import models

class Actividades(models.Model):
    nombre = models.CharField(max_length=30)
    dia = models.CharField(max_length=30)
    horario = models.IntegerField(default=18)
    cupo = models.IntegerField(default=15)

    def __str__(self):
        return f"'Nombre:'{self.nombre} - 'Dia:'{self.dia} - 'Horario (hs):'{self.horario} - 'Cupo:'{self.cupo}" 

class Socios(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(null= True)
    cuota_paga = models.BooleanField()

    def __str__(self):
        return f"'Nombre:'{self.nombre} - 'Apellido:'{self.apellido} - 'Email:'{self.email} - 'Cuota paga:'{self.cuota_paga}" 

class Planes(models.Model):
    nombre = models.CharField(max_length=30)
    cantidad_clases = models.IntegerField(default=30)
    precio = models.IntegerField(blank=True)

    def __str__(self):
        return f"'Nombre:'{self.nombre} - 'Cantidad:'{self.cantidad_clases} - 'Precio: $'{self.precio}" 
    
