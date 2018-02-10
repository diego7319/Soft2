from django.db import models
from django.contrib import admin

class usuariocuenta(models.Model):
    usuario = models.CharField(max_length=30,unique=True)
    dinerocuenta =models.FloatField(default=0)
    def __str__(self):
        return "%s %d" % (self.usuario,self.dinerocuenta)
