from django.db import models
from mongoengine import Document, StringField, DateTimeField, BooleanField

# Create your models here.
class Accion(Document):
    tipo = StringField()
    usuario = StringField()
    hora = DateTimeField()

    meta = {'collection': 'accion', 'allow_inheritance': True}

class VistaAccion(Accion):
    pagina = StringField()

class RegistroAccion(Accion):
    pass

class LoginAccion(Accion):
    pass

class LogoutAccion(Accion):
    pass

class InvitacionAccion(Accion):
    target = StringField()
    grupo = StringField()

class RespuestaInvitacionAccion(Accion):
    grupo = StringField()
    respuesta = BooleanField()

class CrearGrupoAccion(Accion):
    grupo = StringField()
