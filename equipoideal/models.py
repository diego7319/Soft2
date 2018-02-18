from django.db import models

# Create your models here.

class JugadorPais(models.Model):
    nombre = models.CharField(max_length=70)
    pais = models.CharField(max_length=70)
    def __str__(self):
        return "%s %s" % (self.nombre,self.pais)

class Partido(models.Model):
    equipo1 = models.CharField(max_length=30)
    equipo2 = models.CharField(max_length=30)
    fecha = models.DateField()
    Grupo = models.CharField(max_length=1)
    def __str__(self):
        return "%s %s %s %s" % (self.equipo1,self.equipo2,self.fecha,self.Grupo)
