from flask import Blueprint, render_template
from utils.decorators import login_required
from models.seleccion import Seleccion

seleccion_bp = Blueprint('seleccion', __name__, url_prefix='/selecciones')

@seleccion_bp.route('/ver_selecciones')
@login_required
def get_selecciones():
    selecciones = Seleccion.query.all()
    return render_template('selecciones.html', selecciones=selecciones)

@seleccion_bp.route('/<int:id>')
@login_required
def get_seleccion(id):
    seleccion = Seleccion.query.get(id)
    return render_template('detalle_seleccion.html', seleccion=seleccion)