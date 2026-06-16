from models.jugadores import Jugador, Arquero, Defensor, Mediocampista, Delantero
from models.db import db


# Crear jugador
def crear_jugador(data):
    try:
        clases = {
            "arquero": Arquero,
            "defensor": Defensor,
            "mediocampista": Mediocampista,
            "delantero": Delantero
        }

        tipo = data.get("tipo")

        if tipo not in clases:
            return {"error": "Tipo inválido. Debe ser arquero, defensor, mediocampista o delantero"}

        # verificar dorsal duplicado en la misma seleccion
        dorsal_existe = Jugador.query.filter_by(
            seleccion_id=data.get("seleccion_id"),
            num_camiseta=data.get("num_camiseta")
        ).first()
        if dorsal_existe:
            return {"error": f"El dorsal {data.get('num_camiseta')} ya está en uso en esa selección"}

        ClaseJugador = clases[tipo]  # renombrado para no pisar la clase Jugador

        jugador = ClaseJugador(
            nombre=data.get("nombre"),
            edad=data.get("edad"),
            num_camiseta=data.get("num_camiseta"),
            seleccion_id=data.get("seleccion_id")
        )

        db.session.add(jugador)
        db.session.commit()

        return {
            "mensaje": "Jugador creado correctamente",
            "jugador": jugador.serialize()
        }

    except ValueError as error:
        return {"error": str(error)}
    except Exception as error:
        db.session.rollback()
        return {"error": str(error)}


# Obtener jugador por id
def obtener_jugador(id):
    jugador = Jugador.query.get(id)
    if jugador:
        return jugador.serialize()
    return {"error": "Jugador no encontrado"}


# Obtener todos los jugadores
def obtener_jugadores():
    jugadores = Jugador.query.all()
    return [jugador.serialize() for jugador in jugadores]


# Actualizar jugador
def actualizar_jugador(id, data):
    try:
        jugador = Jugador.query.get(id)

        if not jugador:
            return {"error": "Jugador no encontrado"}

        # verificar dorsal duplicado en la misma seleccion al editar
        if "num_camiseta" in data and "seleccion_id" in data:
            dorsal_existe = Jugador.query.filter_by(
                seleccion_id=data.get("seleccion_id"),
                num_camiseta=data.get("num_camiseta")
            ).filter(Jugador.id != id).first()
            if dorsal_existe:
                return {"error": f"El dorsal {data.get('num_camiseta')} ya está en uso en esa selección"}

        campos_permitidos = {
            "nombre": str,
            "edad": int,
            "num_camiseta": int,
            "seleccion_id": int
        }

        for key, value in data.items():
            if key in campos_permitidos and isinstance(value, campos_permitidos[key]):
                setattr(jugador, key, value)

        db.session.commit()
        return jugador.serialize()

    except Exception as error:
        db.session.rollback()
        return {"error": str(error)}


# Eliminar jugador
def eliminar_jugador(id):
    try:
        jugador = Jugador.query.get(id)
        if not jugador:
            return {"error": "Jugador no encontrado"}
        db.session.delete(jugador)
        db.session.commit()
        return {"mensaje": "Jugador eliminado correctamente"}
    except Exception as error:
        db.session.rollback()
        return {"error": str(error)}