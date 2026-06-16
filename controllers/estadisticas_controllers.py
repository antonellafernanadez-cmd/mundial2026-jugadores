from models.estadisticas import Estadistica
from models.jugadores import Jugador
from models.seleccion import Seleccion
from models.db import db

# Crear estadistica para un jugador
def crear_estadistica(data):
    try:
        jugador_id = data.get("jugador_id")
 
        # verificar que el jugador existe antes de crear la estadistica
        jugador = Jugador.query.get(jugador_id)
        if not jugador:
            return {"error": "El jugador no existe"}
 
        # verificar que el jugador no tenga ya una estadistica
        existe = Estadistica.query.filter_by(jugador_id=jugador_id).first()
        if existe:
            return {"error": "Este jugador ya tiene una estadística"}
 
        nueva_estadistica = Estadistica(
            jugador_id=jugador_id,
            goles=data.get("goles", 0),
            asistencias=data.get("asistencias", 0),
            efectividad_pases=data.get("efectividad_pases", 0),
            faltas=data.get("faltas", 0),
            tarj_amarillas=data.get("tarj_amarillas", 0),
            tarj_rojas=data.get("tarj_rojas", 0)
        )
 
        db.session.add(nueva_estadistica)
        db.session.commit()
 
        return {
            "mensaje": "Estadística creada correctamente",
            "estadistica": nueva_estadistica.serialize()
        }
 
    except ValueError as error:
        return {"error": str(error)}
    except Exception as error:
        db.session.rollback()
        return {"error": str(error)}


def obtener_estadistica_por_jugador(jugador_id):
    estadistica = Estadistica.query.filter_by(jugador_id=jugador_id).first()

    if not estadistica:
        return {"error": "Estadística no encontrada"}

    return estadistica.serialize()

def actualizar_estadistica(jugador_id, data):
    estadistica = Estadistica.query.filter_by(jugador_id=jugador_id).first()

    if not estadistica:
        return {"error": "Estadística no encontrada"}

    tipos = {
        "goles": int,
        "asistencias": int,
        "efectividad_pases": int,
        "faltas": int,
        "tarj_amarillas": int,
        "tarj_rojas": int
    }

    for key, value in data.items():
        if key in tipos and isinstance(value, tipos[key]):
            if value < 0:
                return {"error": f"{key} no puede ser negativo"}
            setattr(estadistica, key, value)

    db.session.commit()

    return {
        "mensaje": "Estadística actualizada",
        "estadistica": estadistica.serialize()
    }