from app import app
from models.db import db
from models.usuario import Usuario

def crear_admin():
    with app.app_context():
        # verificar que no exista ya
        existe = Usuario.query.filter_by(email="admin@mundial.com").first()
        if existe:
            print("Ya existe un admin con ese email.")
            return

        admin = Usuario(
            username="admin",
            password="admin123",
            email="admin@mundial.com",
            role="admin"
        )
        db.session.add(admin)
        db.session.commit()
        print("Admin creado correctamente.")
        print("Email: admin@mundial.com")
        print("Password: admin123")

if __name__ == "__main__":
    crear_admin()