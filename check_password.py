from app import app
from models.usuario import Usuario

with app.app_context():
    u = Usuario.query.filter_by(email='uno@gmail.com').first()
    print("Hash guardado:", u.password_hash)
    print("Coincide:", u.check_password('test1234'))
