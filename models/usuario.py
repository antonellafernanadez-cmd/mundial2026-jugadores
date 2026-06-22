from models.db import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), default='user', nullable=False) #admin, entrenador, jugador
    aprobado = db.Column(db.Boolean, default=False, nullable=False) #nuevo campo para controlar si el usuario ha sido aprobado por un admin

    def __init__(self, username, password, email, role='user'):
        if not username:
            raise ValueError("El nombre de usuario es obligatorio")
        if not email:
            raise ValueError("El email es obligatorio")
        if role not in ['admin', 'user']:
            raise ValueError("Rol inválido")
 
        self.username = username
        self.email = email
        self.role = role
        self.set_password(password)  # hashea la contraseña al crear el usuario
        self.aprobado = (role == 'admin')  # admins se aprueban solos

    def set_password(self, password): #Genera un hash seguro para la contraseña
        self.password_hash = generate_password_hash(password)

    def check_password(self, password): #Verifica si la contraseña ingresada coincide con el hash guardado.
        return check_password_hash(self.password_hash, password)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email":self.email,
            "role": self.role,
            "aprobado": self.aprobado
        }
