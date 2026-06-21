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
            session['role'] = user.role  #guarda admin o user
            return redirect(url_for('routes_auth.bienvenida'))
        else:
            return render_template('login.html', error="Credenciales inválidas")
    return render_template('login.html')

@auth_bp.route('/bienvenida')
def bienvenida():
    # Seguridad: Si no está logueado, rebota al login
    if 'user_id' not in session:
        return redirect(url_for('routes_auth.login'))
    
    return render_template('bienvenida.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('routes_auth.login'))