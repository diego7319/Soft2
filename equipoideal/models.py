from django.db import models

# Create your models here.

class JugadorPais(models.Model):
    nombre = models.CharField(max_length=70)
    pais = models.CharField(max_length=70)
    def __str__(self):
        return "%s %s" % (self.nombre,self.pais)
