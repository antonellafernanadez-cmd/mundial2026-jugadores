import os
import time
import requests
from dotenv import load_dotenv
from app import app
from models.db import db
from models.seleccion import Seleccion
from models.jugadores import Arquero, Defensor, Mediocampista, Delantero
from models.estadisticas import Estadistica

load_dotenv()

API_KEY = os.getenv("API_FOOTBALL_KEY")
BASE_URL = "https://v3.football.api-sports.io"
HEADERS = {
    "x-apisports-key":API_KEY
}

SELECCIONES = [
    {"team_id": 26,  "pais": "Argentina",     "entrenador": "Lionel Scaloni"},
    {"team_id": 6,   "pais": "Brasil",         "entrenador": "Dorival Junior"},
    {"team_id": 2,   "pais": "Francia",        "entrenador": "Didier Deschamps"},
    {"team_id": 9,   "pais": "España",         "entrenador": "Luis de la Fuente"},
    {"team_id": 25,  "pais": "Alemania",       "entrenador": "Julian Nagelsmann"},
    {"team_id": 27,  "pais": "Portugal",       "entrenador": "Roberto Martinez"},
    {"team_id": 10,  "pais": "Inglaterra",     "entrenador": "Thomas Tuchel"},
    {"team_id": 17,  "pais": "Uruguay",        "entrenador": "Marcelo Bielsa"},
    {"team_id": 16,  "pais": "Mexico",         "entrenador": "Javier Aguirre"},
    {"team_id": 1,   "pais": "Estados Unidos", "entrenador": "Mauricio Pochettino"},
]

POSICION_A_TIPO = {
    "Goalkeeper": "arquero",
    "Defender":   "defensor",
    "Midfielder": "mediocampista",
    "Attacker":   "delantero"
}

CLASES_JUGADOR = {
    "arquero":       Arquero,
    "defensor":      Defensor,
    "mediocampista": Mediocampista,
    "delantero":     Delantero
}

def fetch_jugadores(team_id):
    """Llama a la API y devuelve la lista de jugadores de una selección."""
    url = f"{BASE_URL}/players/squads"
    params = {"team": team_id}

    print(f"  Llamando a la API: {url} con team_id={team_id}")

    try:
        response = requests.get(url, headers=HEADERS, params=params)
        print(f"  Status: {response.status_code}")
        print(f"  Respuesta raw: {response.text[:300]}")  # muestra los primeros 300 caracteres

        if response.status_code == 429:
            print("  Límite de requests alcanzado, esperando 10 segundos...")
            time.sleep(10)
            response = requests.get(url, headers=HEADERS, params=params)
            print(f"  Status reintento: {response.status_code}")

        if response.status_code != 200:
            print(f"  ERROR: status {response.status_code}")
            return []

        data = response.json()

        if not data.get("response"):
            print(f"  ERROR: respuesta vacía de la API: {data}")
            return []

        jugadores = data["response"][0]["players"]
        print(f"  Jugadores recibidos: {len(jugadores)}")
        return jugadores

    except Exception as e:
        print(f"  EXCEPCIÓN: {str(e)}")
        return []

def populate_seleccion(info):
    """Crea una selección y sus jugadores en la base de datos."""
    pais = info["pais"]
    entrenador = info["entrenador"]
    team_id = info["team_id"]

    existe = Seleccion.query.filter_by(pais=pais).first()
    if existe:
        print(f"  Ya existe: {pais}, saltando...")
        return 0

    seleccion = Seleccion(pais=pais, entrenador=entrenador)
    db.session.add(seleccion)
    db.session.flush()
    print(f"  Selección creada: {pais} (id={seleccion.id})")

    # Pausa antes de llamar a la API para no superar el límite
    time.sleep(3)

    jugadores_raw = fetch_jugadores(team_id)
    jugadores_creados = 0

    for j in jugadores_raw:
        nombre = j.get("name")
        edad = j.get("age")
        num_camiseta = j.get("number") or 0
        posicion = j.get("position")
        tipo = POSICION_A_TIPO.get(posicion, "defensor")

        if not nombre or not edad:
            continue

        ClaseJugador = CLASES_JUGADOR[tipo]
        jugador = ClaseJugador(
            nombre=nombre,
            edad=edad,
            num_camiseta=num_camiseta,
            seleccion_id=seleccion.id
        )
        db.session.add(jugador)
        db.session.flush()

        estadistica = Estadistica(jugador_id=jugador.id)
        db.session.add(estadistica)

        jugadores_creados += 1
        print(f"    Jugador creado: {nombre} ({tipo})")

    return jugadores_creados

def populate_all():
    with app.app_context():
        print("=== Iniciando carga de datos desde API-Football ===\n")

        total_jugadores = 0

        for info in SELECCIONES:
            print(f"Procesando: {info['pais']}")
            jugadores = populate_seleccion(info)
            total_jugadores += jugadores
            print()

        print("Haciendo commit a la base de datos...")
        db.session.commit()
        print(f"=== Carga completa: {len(SELECCIONES)} selecciones, {total_jugadores} jugadores ===")

if __name__ == "__main__":
    populate_all()