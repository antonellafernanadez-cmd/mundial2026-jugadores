from models.seleccion import Seleccion
from models.db import db

# Obtener todas las selecciones
def obtener_selecciones():
    selecciones = Seleccion.query.all()
    return [seleccion.serialize() for seleccion in selecciones]
 
 
# Obtener una seleccion por id
def obtener_seleccion(id):
    seleccion = Seleccion.query.get(id)
    if seleccion:
        return seleccion.serialize()
    return {"error": "Seleccion no encontrada"}