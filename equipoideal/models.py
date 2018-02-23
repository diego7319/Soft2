from django.db import models

# Create your models here.

class JugadorPais(models.Model):
    nombre = models.CharField(max_length=70)
    pais = models.CharField(max_length=70)
    def __str__(self):
        return "%s %s" % (self.nombre,self.pais)

class scoreEI(models.Model):
    idEI= models.AutoField(primary_key=True)
    grupo=models.CharField(max_length=30)
    user=models.CharField(max_length=20)
    sala=models.CharField(max_length=20)
    puntaje=models.FloatField()

class salaEI(models.Model):
    idjuego=models.AutoField(primary_key=True)
    nombreJuego=models.CharField(max_length=30)
    grupo=models.CharField(max_length=30)
    #activo o desactivado
    estado=models.CharField(max_length=11)
    pago=models.IntegerField(default=0)

class PagoSalaEI(models.Model):
    idjuego=models.AutoField(primary_key=True)
    nombreJuego=models.CharField(max_length=30)
    grupo=models.CharField(max_length=30)
    user=models.CharField(max_length=20)
    #Pagado o deuda
    estadopago=models.CharField(max_length=10)
#Guarda el dinero de las apuestas

class SalaApuestasEI(models.Model):
    idjuego=models.AutoField(primary_key=True)
    nombreJuego=models.CharField(max_length=30)
    grupo=models.CharField(max_length=30)

class resultadosEI(models.Model):
    idresultado=models.AutoField(primary_key=True)
    nombreJuego=models.CharField(max_length=30)
    grupo=models.CharField(max_length=30)
    user=models.CharField(max_length=20)
    pago=models.IntegerField()

class ScorejuegoEI(models.Model):
    idjuego=models.AutoField(primary_key=True)
    user=models.CharField(max_length=20)
    grupo=models.CharField(max_length=30)
    resultado=models.FloatField(default=0)
    nombreJuego=models.CharField(max_length=30)

class Pozo_salaEI(models.Model):
    idjuego=models.AutoField(primary_key=True)
    nombreJuego=models.CharField(max_length=30)
    dinero=models.FloatField()


class notificacionesEI(models.Model):
    idnotificacion=models.AutoField(primary_key=True)
    user=models.CharField(max_length=20)
    #se muestran  en notificaciones estado='0'
    estado=models.CharField(max_length=1,default='1')
    sala=models.CharField(max_length=30,default="")
    ganador=models.CharField(max_length=2,default='no')
