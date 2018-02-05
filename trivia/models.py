from django.db import models
#Preguntas
class PreguntaTrivia(models.Model):
    idPregunta = models.AutoField(primary_key=True)
    descPregunta = models.CharField(max_length=250)
    respuesta=models.CharField(max_length=150)
    incorrecta1=models.CharField(max_length=150)
    incorrecta2=models.CharField(max_length=150)
    incorrecta3=models.CharField(max_length=150)
    def __str__(self):
        return "%s %s" % (self.nombre)
