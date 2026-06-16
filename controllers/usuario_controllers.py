from models.usuario import Usuario
from models.db import db
 
 
# Registrar nuevo usuario
def registrar_usuario(data):
    try:
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")
        role = data.get("role", "user")  # por defecto es user
 
        # verificar que no falten datos
        if not username or not password or not email:
            return {"error": "Username, password y email son obligatorios"}
 
        # verificar que el username no esté en uso
        if Usuario.query.filter_by(username=username).first():
            return {"error": "El nombre de usuario ya está en uso"}
 
        # verificar que el email no esté en uso
        if Usuario.query.filter_by(email=email).first():
            return {"error": "El email ya está registrado"}
 
        nuevo_usuario = Usuario(
            username=username,
            password=password,
            email=email,
            role=role
        )
 
        db.session.add(nuevo_usuario)
        db.session.commit()
 
        return {
            "mensaje": "Usuario registrado correctamente",
            "usuario": nuevo_usuario.serialize()
        }
 
    except ValueError as error:
        return {"error": str(error)}
    except Exception as error:
        db.session.rollback()
        return {"error": str(error)}
 
 
# Login
def login_usuario(data):
    try:
        username = data.get("username")
        password = data.get("password")
 
        if not username or not password:
            return {"error": "Username y password son obligatorios"}
 
        # buscar el usuario por username
        usuario = Usuario.query.filter_by(username=username).first()
 
        # verificar que existe y que la contraseña es correcta
        if not usuario or not usuario.check_password(password):
            return {"error": "Usuario o contraseña incorrectos"}
 
        return {
            "mensaje": "Login exitoso",
            "usuario": usuario.serialize()
        }
 
    except Exception as error:
        return {"error": str(error)}
 
 
# Obtener todos los usuarios (solo admin)
def obtener_usuarios():
    usuarios = Usuario.query.all()
    return [usuario.serialize() for usuario in usuarios]
 
 
# Obtener usuario por id (solo admin)
def obtener_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        return usuario.serialize()
    return {"error": "Usuario no encontrado"}
 
 
# Eliminar usuario (solo admin)
def eliminar_usuario(id):
    try:
        usuario = Usuario.query.get(id)
 
        if not usuario:
            return {"error": "Usuario no encontrado"}
 
        db.session.delete(usuario)
        db.session.commit()
        return {"mensaje": "Usuario eliminado correctamente"}
 
    except Exception as error:
        db.session.rollback()
        return {"error": str(error)}