from django.db import models


#Preguntas
#idPregunta se genera automaticamente
'''para agregar pregunta:
>> from trivia.models import PreguntaTrivia
>> pregunta1 = PreguntaTrivia(descPregunta='¿Qué número de Mundial será Rusia 2018',respuesta='21',incorrecta1='18',incorrecta2='24',incorrecta3='20')
>> pregunta1.save()
'''
class PreguntaTrivia(models.Model):
    idPregunta = models.AutoField(primary_key=True)
    descPregunta = models.CharField(max_length=250)
    respuesta=models.CharField(max_length=150)
    incorrecta1=models.CharField(max_length=150)
    incorrecta2=models.CharField(max_length=150)
    incorrecta3=models.CharField(max_length=150)
    def __str__(self):
        return "%s %s" % (self.idPregunta, self.descPregunta)

#DB para puntaje global

class scoretrivia(models.Model):
    idtrivia= models.AutoField(primary_key=True)
    grupo=models.CharField(max_length=30)
    user=models.CharField(max_length=20)
    sala=models.CharField(max_length=20)
    puntaje=models.FloatField()
    idjueg=models.ForeignKey('salatrivia', on_delete=models.CASCADE)

class salatrivia(models.Model):
    idjuego=models.AutoField(primary_key=True)
    nombreJuego=models.CharField(max_length=30)
    grupo=models.CharField(max_length=30)
    cantpreguntas=models.IntegerField()
    #activo o desactivado
    estado=models.CharField(max_length=11)
    pago=models.IntegerField(default=0)

class PagoSala(models.Model):
    idjuego=models.AutoField(primary_key=True)
    nombreJuego=models.CharField(max_length=30)
    grupo=models.CharField(max_length=30)
    user=models.CharField(max_length=20)
    #Pagado o deuda
    estadopago=models.CharField(max_length=10)
#Guarda el dinero de las apuestas

class SalaApuestas(models.Model):
    idjuego=models.AutoField(primary_key=True)
    nombreJuego=models.CharField(max_length=30)
    grupo=models.CharField(max_length=30)

class resultados(models.Model):
    idresultado=models.AutoField(primary_key=True)
    nombreJuego=models.CharField(max_length=30)
    grupo=models.CharField(max_length=30)
    user=models.CharField(max_length=20)
    pago=models.IntegerField()

class Scorejuego(models.Model):
    idjuego=models.AutoField(primary_key=True)
    user=models.CharField(max_length=20)
    grupo=models.CharField(max_length=30)
    resultado=models.FloatField(default=0)
    nombreJuego=models.CharField(max_length=30)

class Pozo_sala(models.Model):
    idjuego=models.AutoField(primary_key=True)
    nombreJuego=models.CharField(max_length=30)
    dinero=models.FloatField()

class notificaciones(models.Model):
    idnotificacion=models.AutoField(primary_key=True)
    user=models.CharField(max_length=20)
    #se muestran  en notificaciones estado='0'
    estado=models.CharField(max_length=1,default='1')
    sala=models.CharField(max_length=30,default="")
    ganador=models.CharField(max_length=2,default='no')
