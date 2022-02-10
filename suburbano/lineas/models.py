from django.db import models

# Create your models here.
class Linea(models.Model):
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Estacion(models.Model):
    nombre = models.CharField(max_length=255)
    linea = models.ForeignKey(Linea, on_delete=models.CASCADE, related_name='estaciones')
    distancia_anterior = models.FloatField(default=0)
    estacion_anterior = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Pasajero(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)

class Viaje(models.Model):
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE, related_name="viajes")
    fecha_inicio = models.DateTimeField()
    estacion_inicio = models.ForeignKey(Estacion, on_delete=models.CASCADE, related_name="viajes_iniciados")
    fecha_final = models.DateTimeField()
    estacion_final = models.ForeignKey(Estacion, on_delete=models.CASCADE, related_name="viajes_finalizados")