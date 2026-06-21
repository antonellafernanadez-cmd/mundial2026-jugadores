from models.db import db
from config.config import DATABASE_CONNECTION_URI
from flask import Flask, render_template
from routes.routes_auth import auth_bp
from routes.routes_estadisticas import estadisticas_bp
from routes.routes_jugadores import jugadores_bp
from routes.routes_seleccion import seleccion_bp
from routes.routes_usuario import users_bp
from utils.banderas import url_bandera
app= Flask(__name__)

app.config["SECRET_KEY"]="mundial_2026"
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(jugadores_bp)
app.register_blueprint(estadisticas_bp)
app.register_blueprint(seleccion_bp)
app.register_blueprint(users_bp)

# Filtro de Jinja: permite usar {{ pais | bandera }} en cualquier template
app.jinja_env.filters['bandera'] = url_bandera

with app.app_context():
    from models.usuario import Usuario
    from models.seleccion import Seleccion
    from models.jugadores import Jugador, Arquero, Defensor, Mediocampista, Delantero
    from models.estadisticas import Estadistica
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

if __name__=="__main__":
    app.run(debug=True)