from flask import Blueprint, render_template, redirect, request, url_for, session
from models.db import db
from models.usuario import Usuario
from utils.decorators import *

users_bp = Blueprint('users_bp', __name__, url_prefix='/users')


# Ver todos los usuarios (solo admin)
@users_bp.route('/')
@login_required
@admin_required
def get_users():
    users = Usuario.query.all()
    return render_template('usuarios.html', users=users)


# Eliminar usuario (solo admin)
@users_bp.route('/delete/<int:id>')
@login_required
@admin_required
def delete_user(id):
    user = Usuario.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('users_bp.get_users'))


# Editar usuario - formulario (solo admin)
@users_bp.route('/update/<int:id>', methods=['GET'])
@login_required
@admin_required
def edit_user(id):
    user = Usuario.query.get(id)
    return render_template('edit_usuarios.html', user=user)


# Editar usuario - guardar cambios (solo admin)
@users_bp.route('/update/<int:id>', methods=['POST'])
@login_required
@admin_required
def update_user(id):
    user = Usuario.query.get(id)
    user.username = request.form['username']
    user.email = request.form['email']
    user.role = request.form['role']
    user.set_password(request.form['password'])  # hashea la contraseña correctamente
    db.session.commit()
    return redirect(url_for('users_bp.get_users'))


# Registro de nuevo usuario
@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        existing_user = Usuario.query.filter_by(email=email).first()
        if existing_user:
            return render_template('register.html', error="El usuario ya existe")

        new_user = Usuario(username=username, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('routes_auth.login'))

    return render_template('register.html')