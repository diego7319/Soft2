from django.db import models

# Create your models here.

class grupo(models.Model):
    nombre = models.CharField(max_length=30,unique=True)
    owner=models.CharField(max_length=30)
    def __str__(self):
        return "%s %s" % (self.nombre)

class Invitacion(models.Model):
    invitado = models.CharField(max_length=10)
    owner = models.CharField(max_length=300)
    grupo = models.ManyToManyField(grupo)
    def __str__(self):
        return self.headline
