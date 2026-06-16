from models.db import db


class Jugador(db.Model):
    __tablename__ = "jugadores"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    num_camiseta = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(50))  # columna discriminadora para polimorfismo
    seleccion_id = db.Column(db.Integer, db.ForeignKey("selecciones.id"), nullable=True) # Clave foránea hacia selecciones
    estadistica = db.relationship("Estadistica", backref="jugador", uselist=False) # Relación 1 a 1 con Estadistica

    __mapper_args__ = {
        'polymorphic_identity': 'jugador', #es el tipo de cada jugador, cuando sea el tipo por ej: Arquero crea el objeto Arquero
        'polymorphic_on': tipo #se utiliza la columna tipo para diferenciar
    }

    #usamos un campo discrimador "tipo", junto con __mapper_args__ para implemetar el polifirmismo en SQLAlchemy
    #permitiendo que múltiples clases hereden de una misma tabla

    def __init__(self, nombre, edad, num_camiseta, seleccion_id=None):
        if not nombre:
            raise ValueError("El nombre es obligatorio")
        if edad < 15:
            raise ValueError("Edad inválida")
        if num_camiseta <= 0:
            raise ValueError("Número de camiseta inválido")

        self.nombre = nombre
        self.edad = edad
        self.num_camiseta = num_camiseta
        self.seleccion_id = seleccion_id

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "edad": self.edad,
            "num_camiseta": self.num_camiseta,
            "tipo": self.tipo,
            "seleccion_id": self.seleccion_id,
            "estadistica": self.estadistica.serialize() if self.estadistica else None
        }


class Arquero(Jugador):
    __mapper_args__ = {
        'polymorphic_identity': 'arquero'
    }

    def __init__(self, nombre, edad, num_camiseta, seleccion_id=None):
        super().__init__(nombre, edad, num_camiseta, seleccion_id)


class Defensor(Jugador):
    __mapper_args__ = {
        'polymorphic_identity': 'defensor'
    }

    def __init__(self, nombre, edad, num_camiseta, seleccion_id=None):
        super().__init__(nombre, edad, num_camiseta, seleccion_id)


class Mediocampista(Jugador):
    __mapper_args__ = {
        'polymorphic_identity': 'mediocampista'
    }

    def __init__(self, nombre, edad, num_camiseta, seleccion_id=None):
        super().__init__(nombre, edad, num_camiseta, seleccion_id)


class Delantero(Jugador):
    __mapper_args__ = {
        'polymorphic_identity': 'delantero'
    }

    def __init__(self, nombre, edad, num_camiseta, seleccion_id=None):
        super().__init__(nombre, edad, num_camiseta, seleccion_id)

    #cuando se crea un jugador desde el controllers, automaticamente se guarda con el tipo.