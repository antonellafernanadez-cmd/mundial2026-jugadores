from models.db import db
from config.config import DATABASE_CONNECTION_URI
from flask import Flask

app=Flask(__name__)

app.config["SECRET_KEY"]="mundial_2026"
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.app_context():
    from models.usuario import Usuario
    from models.seleccion import Seleccion
    from models.jugadores import Jugador, Arquero, Defensor, Mediocampista, Delantero
    from models.estadisticas import Estadistica
    db.create_all()

if __name__=="__main__":
    app.run(debug=True)