from flask import Blueprint, render_template, redirect, request, url_for, session
from models.db import db
from models.jugadores import Jugador, Arquero, Defensor, Mediocampista, Delantero
from models.seleccion import Seleccion
from utils.decorators import login_required, admin_required
from controllers.jugadores_controllers import *

jugadores_bp = Blueprint('jugadores', __name__, url_prefix='/jugadores')


# Ver todos los jugadores ordenados por seleccion y numero de camiseta
@jugadores_bp.route('/ver_jugadores')
@login_required
def get_jugadores():
    jugadores = Jugador.query.order_by(Jugador.seleccion_id, Jugador.tipo, Jugador.num_camiseta).all()
    return render_template('jugadores.html', jugadores=jugadores)


# Ver detalle de un jugador
@jugadores_bp.route('/detalle/<int:id>')
@login_required
def get_jugador(id):
    jugador = Jugador.query.get(id)
    if not jugador:
        return redirect(url_for('jugadores.get_jugadores'))
    return render_template('detalle_jugador.html', jugador=jugador)


# Crear jugador - formulario (solo admin)
@jugadores_bp.route('/crear', methods=['GET'])
@login_required
@admin_required
def crear_jugador_form():
    selecciones = Seleccion.query.all()
    return render_template('formulario_jugador.html', selecciones=selecciones)


# Crear jugador - guardar (solo admin)
@jugadores_bp.route('/crear', methods=['POST'])
@login_required
@admin_required
def crear_jugador_post():
    data = {
        "nombre": request.form['nombre'],
        "edad": int(request.form['edad']),
        "num_camiseta": int(request.form['num_camiseta']),
        "tipo": request.form['tipo'],
        "seleccion_id": int(request.form['seleccion_id'])
    }
    resultado = crear_jugador(data)
    if "error" in resultado:
        selecciones = Seleccion.query.all()
        return render_template('formulario_jugador.html', error=resultado["error"], selecciones=selecciones)
    return redirect(url_for('jugadores.get_jugadores'))


# Editar jugador - formulario (solo admin)
@jugadores_bp.route('/editar/<int:id>', methods=['GET'])
@login_required
@admin_required
def editar_jugador_form(id):
    jugador = Jugador.query.get(id)
    selecciones = Seleccion.query.all()
    return render_template('jugador_editar.html', jugador=jugador, selecciones=selecciones)


# Editar jugador - guardar (solo admin)
@jugadores_bp.route('/editar/<int:id>', methods=['POST'])
@login_required
@admin_required
def editar_jugador_post(id):
    data = {
        "nombre": request.form['nombre'],
        "edad": int(request.form['edad']),
        "num_camiseta": int(request.form['num_camiseta']),
        "seleccion_id": int(request.form['seleccion_id'])
    }
    resultado = actualizar_jugador(id, data)
    if "error" in resultado:
        jugador = Jugador.query.get(id)
        selecciones = Seleccion.query.all()
        return render_template('jugador_editar.html', error=resultado["error"], jugador=jugador, selecciones=selecciones)
    return redirect(url_for('jugadores.get_jugadores'))


# Eliminar jugador (solo admin)
@jugadores_bp.route('/eliminar/<int:id>')
@login_required
@admin_required
def eliminar_jugador_route(id):
    eliminar_jugador(id)
    return redirect(url_for('jugadores.get_jugadores'))