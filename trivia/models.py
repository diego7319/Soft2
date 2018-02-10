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

class scoretrivia(models.Model):
    idPregunta = models.AutoField(primary_key=True)
    grupo=models.CharField(max_length=30)
    user=models.CharField(max_length=20)
    puntaje=models.CharField(max_length=2)
    idpreguntaTrivia=models.CharField(max_length=10)

class juegostrivia(models.Model):
    idjuego=models.AutoField(primary_key=True)
    nombreJuego=models.CharField(max_length=30)
    grupo=models.CharField(max_length=30)
    #activo o desactivado
    estado=models.CharField(max_length=11)
