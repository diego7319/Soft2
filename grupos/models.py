from django.db import models

# Create your models here.

class grupo(models.Model):
    nombre = models.CharField(max_length=30,unique=True)
    owner=models.CharField(max_length=30)
    def __str__(self):
        return "%s %s" % (self.nombre)

class Invitacion(models.Model):
    invitado = models.CharField(max_length=10)
    owner = models.CharField(max_length=30)
    grupo=models.CharField(max_length=30)
    estado=models.CharField(max_length=11,default='pendiente')
    #grupo = models.ManyToManyField(grupo)
    #estados rechazado y aceptado
    def __str__(self):
        return (invitado)
