from django.db import models

# Create your models here.

class Partido(models.Model):
    idPartido = models.AutoField(primary_key=True)
    equipo1 = models.CharField(max_length=30)
    equipo2 = models.CharField(max_length=30)
    monto1=models.FloatField()
    monto2=models.FloatField()
    montoempate=models.FloatField()
    estado=models.BooleanField(default=True)
    fecha = models.DateField()
    Grupo = models.CharField(max_length=1)
    def __str__(self):
        return "%s %s %s %s" % (self.equipo1,self.equipo2,self.fecha,self.Grupo)
