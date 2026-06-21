from app import app
from models.db import db
from models.usuario import Usuario

with app.app_context():
    u = Usuario.query.filter_by(email='uno@gmail.com').first()
    if u:
        db.session.delete(u)
        db.session.commit()
        print("Usuario eliminado")
    else:
        print("No se encontró el usuario")
