from models.db import db
 
class Estadistica(db.Model):
    __tablename__ = "estadisticas"
 
    id = db.Column(db.Integer, primary_key=True)
    goles = db.Column(db.Integer, default=0)
    asistencias = db.Column(db.Integer, default=0)
    efectividad_pases = db.Column(db.Integer, default=0)  # se utiliza default para evitar el null en la db
    faltas = db.Column(db.Integer, default=0)
    tarj_rojas = db.Column(db.Integer, default=0)
    tarj_amarillas = db.Column(db.Integer, default=0)
 
    # Clave foránea: conecta con la tabla jugadores
    jugador_id = db.Column(db.Integer, db.ForeignKey("jugadores.id"), nullable=False)
 
    def __init__(self, jugador_id, goles=0, asistencias=0, efectividad_pases=0, faltas=0, tarj_rojas=0, tarj_amarillas=0):
        if not jugador_id:
            raise ValueError("Debe estar asociado a un jugador")
        if goles < 0:
            raise ValueError("Los goles no pueden ser negativos")
        if asistencias < 0:
            raise ValueError("Las asistencias no pueden ser negativas")
        if tarj_amarillas < 0 or tarj_rojas < 0:
            raise ValueError("Las tarjetas no pueden ser negativas")
 
        self.jugador_id = jugador_id
        self.goles = goles
        self.asistencias = asistencias
        self.efectividad_pases = efectividad_pases
        self.faltas = faltas
        self.tarj_rojas = tarj_rojas
        self.tarj_amarillas = tarj_amarillas
 
    def serialize(self):
        return {
            "id": self.id,
            "jugador_id": self.jugador_id,
            "goles": self.goles,
            "asistencias": self.asistencias,
            "efectividad_pases": self.efectividad_pases,
            "faltas": self.faltas,
            "tarj_rojas": self.tarj_rojas,
            "tarj_amarillas": self.tarj_amarillas
        }