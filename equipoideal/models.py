from django.db import models

# Create your models here.

class JugadorPais(models.Model):
    nombre = models.CharField(max_length=70)
    pais = models.CharField(max_length=70)
    def __str__(self):
        return "%s %s" % (self.nombre,self.pais)

class salaequipoideal(models.Model):
    idjuego=models.AutoField(primary_key=True)
    nombreJuego=models.CharField(max_length=30)
    grupo=models.CharField(max_length=30)
    #activo o desactivado
    estado=models.CharField(max_length=11)
    pago=models.IntegerField(default=0)

class PagoSalaEquipoIdeal(models.Model):
    idjuego=models.AutoField(primary_key=True)
    nombreJuego=models.CharField(max_length=30)
    grupo=models.CharField(max_length=30)
    user=models.CharField(max_length=20)
    #Pagado o deuda
    estadopago=models.CharField(max_length=10)
