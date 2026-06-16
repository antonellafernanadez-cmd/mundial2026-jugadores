from models.db import db
 
class Seleccion(db.Model):
    __tablename__ = "selecciones"
 
    id = db.Column(db.Integer, primary_key=True)
    pais = db.Column(db.String(100), nullable=False)
    entrenador = db.Column(db.String(100), nullable=False)
 
    # Relación uno a muchos: una selección tiene muchos jugadores
    jugadores = db.relationship("Jugador", backref="seleccion", lazy='subquery')
 
    def __init__(self, pais, entrenador):
        if not pais:
            raise ValueError("El país es obligatorio")
        if not entrenador:
            raise ValueError("El entrenador es obligatorio")
 
        self.pais = pais
        self.entrenador = entrenador
 
    def serialize(self):
        return {
            "id": self.id,
            "pais": self.pais,
            "entrenador": self.entrenador
        }