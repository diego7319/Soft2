from datetime import datetime
from .models import VistaAccion

def log_accion_ver(db, usuario, pagina):
    hora = datetime.now()
    acc = VistaAccion(tipo="vista", usuario=usuario, hora=hora, pagina=pagina)
    doc = acc.to_mongo()
    collection = db[acc._get_collection_name()]
    collection.insert_one(doc)
