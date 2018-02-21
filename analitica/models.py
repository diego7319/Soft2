from django.db import models
from mongoengine import Document, StringField, DateTimeField

# Create your models here.
class Accion(Document):
    tipo = StringField()
    usuario = StringField()

    meta = {'collection': 'accion', 'allow_inheritance': True}

class VistaAccion(Accion):
    hora = DateTimeField()
    pagina = StringField()

