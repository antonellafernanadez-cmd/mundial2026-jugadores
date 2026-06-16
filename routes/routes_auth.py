from flask import Blueprint, render_template, request, redirect, url_for, session
from models.usuario import Usuario

auth_bp = Blueprint('routes_auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = Usuario.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role
            return redirect(url_for('jugadores.get_jugadores'))  # redirige a lista de jugadores
        else:
            return render_template('login.html', error="Credenciales inválidas")
    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('routes_auth.login'))