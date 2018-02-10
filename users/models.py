from django.db import models

class Cuenta(models.Model):
    usuario = models.CharField(max_length=30,unique=True)
    dinerocuenta =models.FloatField(default=0)
    def __str__(self):
        return "%s %s" (self.usuario,self.dinerocuenta)
