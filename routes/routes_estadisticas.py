from flask import Blueprint, render_template, redirect, request, url_for
from utils.decorators import login_required, admin_required
from controllers.estadisticas_controllers import *

estadisticas_bp = Blueprint('estadisticas', __name__, url_prefix='/estadisticas')


# Ver estadistica de un jugador (cualquier usuario logueado)
@estadisticas_bp.route('/<int:jugador_id>')
@login_required
def get_estadistica(jugador_id):
    estadistica = obtener_estadistica_por_jugador(jugador_id)
    return render_template('formulario_estadisticas.html', estadistica=estadistica, jugador_id=jugador_id)


# Editar estadistica - formulario (solo admin)
@estadisticas_bp.route('/editar/<int:jugador_id>', methods=['GET'])
@login_required
@admin_required
def editar_estadistica_form(jugador_id):
    estadistica = obtener_estadistica_por_jugador(jugador_id)
    return render_template('formulario_estadisticas.html', estadistica=estadistica, jugador_id=jugador_id)


# Editar estadistica - guardar (solo admin)
@estadisticas_bp.route('/editar/<int:jugador_id>', methods=['POST'])
@login_required
@admin_required
def editar_estadistica_post(jugador_id):
    data = {
        "goles": int(request.form.get('goles', 0)),
        "asistencias": int(request.form.get('asistencias', 0)),
        "efectividad_pases": int(request.form.get('efectividad_pases', 0)),
        "faltas": int(request.form.get('faltas', 0)),
        "tarj_amarillas": int(request.form.get('tarj_amarillas', 0)),
        "tarj_rojas": int(request.form.get('tarj_rojas', 0))
    }
    resultado = actualizar_estadistica(jugador_id, data)
    if "error" in resultado:
        estadistica = obtener_estadistica_por_jugador(jugador_id)
        return render_template('formulario_estadisticas.html', error=resultado["error"], estadistica=estadistica, jugador_id=jugador_id)
    return redirect(url_for('jugadores.get_jugador', id=jugador_id))