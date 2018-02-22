from datetime import datetime
from .models import VistaAccion, RegistroAccion, LoginAccion, LogoutAccion, InvitacionAccion, CrearGrupoAccion, RespuestaInvitacionAccion

def log_accion_ver(db, usuario, pagina):
    hora = datetime.now()
    acc = VistaAccion(tipo="vista", usuario=usuario, hora=hora, pagina=pagina)
    doc = acc.to_mongo()
    collection = db[acc._get_collection_name()]
    collection.insert_one(doc)

def get_accion_ver(db):
    acc = VistaAccion()
    doc = acc.to_mongo()
    collection = db[acc._get_collection_name()]
    return collection.find({'tipo':'vista'}).count()

def log_accion_registro(db, usuario):
    hora = datetime.now()
    acc = RegistroAccion(tipo="registro", usuario=usuario, hora=hora)
    doc = acc.to_mongo()
    collection = db[acc._get_collection_name()]
    collection.insert_one(doc)

def get_accion_registro(db):
    acc = RegistroAccion()
    doc = acc.to_mongo()
    collection = db[acc._get_collection_name()]
    return collection.find({'tipo':'registro'}).count()

def log_accion_login(db, usuario):
    hora = datetime.now()
    acc = LoginAccion(tipo="login", usuario=usuario, hora=hora)
    doc = acc.to_mongo()
    collection = db[acc._get_collection_name()]
    collection.insert_one(doc)

def get_accion_login(db):
    acc = LoginAccion()
    doc = acc.to_mongo()
    collection = db[acc._get_collection_name()]
    return collection.find({'tipo':'login'}).count()

def log_accion_logout(db, usuario):
    hora = datetime.now()
    acc = LogoutAccion(tipo="logout", usuario=usuario, hora=hora)
    doc = acc.to_mongo()
    collection = db[acc._get_collection_name()]
    collection.insert_one(doc)

def get_accion_logout(db):
    acc = LogoutAccion()
    doc = acc.to_mongo()
    collection = db[acc._get_collection_name()]
    return collection.find({'tipo':'logout'}).count()

def log_accion_invitar(db, usuario, target, grupo):
    hora = datetime.now()
    acc = InvitacionAccion(tipo="invitar", usuario=usuario, hora=hora, target=target, grupo=grupo)
    doc = acc.to_mongo()
    collection = db[acc._get_collection_name()]
    collection.insert_one(doc)

def get_accion_invitar(db):
    acc = InvitacionAccion()
    doc = acc.to_mongo()
    collection = db[acc._get_collection_name()]
    return collection.find({'tipo':'invitar'}).count()

def log_accion_crear_grupo(db, usuario, grupo):
    hora = datetime.now()
    acc = CrearGrupoAccion(tipo="crear_grupo", usuario=usuario, hora=hora, grupo=grupo)
    doc = acc.to_mongo()
    collection = db[acc._get_collection_name()]
    collection.insert_one(doc)

def get_accion_crear_grupo(db):
    acc = CrearGrupoAccion()
    doc = acc.to_mongo()
    collection = db[acc._get_collection_name()]
    return collection.find({'tipo':'crear_grupo'}).count()

def log_accion_rpta_invitacion(db, usuario, grupo, rpta):
    hora = datetime.now()
    acc = RespuestaInvitacionAccion(tipo="invitar", usuario=usuario, hora=hora, grupo=grupo, respuesta=rpta)
    doc = acc.to_mongo()
    collection = db[acc._get_collection_name()]
    collection.insert_one(doc)

def get_accion_rpta_invitacion(db):
    acc = RespuestaInvitacionAccion()
    doc = acc.to_mongo()
    collection = db[acc._get_collection_name()]
    return collection.find({'tipo':'invitar'}).count()
