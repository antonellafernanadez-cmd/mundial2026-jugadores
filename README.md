# mundial2026-jugadores
Aplicación web mundial 2026 - Parte Jugadores
# Mundial 2026 - Gestión de Jugadores

Aplicación web desarrollada con Flask para gestionar jugadores del Mundial 2026. Permite visualizar selecciones, jugadores y estadísticas, con sistema de autenticación y roles de usuario.

---

# Integrantes del grupo
Antonella Fernandez
Leonel Bustos
Javier Cabrera
Marcelo Britos

---

# Configuración de la app
Antes de ejecutar la aplicación, se debe configurar las siguientes variables de entorno:

MYSQL_USER=<tu_usuario>
MYSQL_PASSWORD=<tu_contraseña>
MYSQL_DATABASE=<nombre_de_la_base>
MYSQL_HOST=<host_de_mysql>
MYSQL_PORT=<puerto_de_mysql>
API_FOOTBALL_KEY= Debe crear una cuenta en API football.com y obtener la clave de la API, con el plan gratuito es suficiente.

---

## Tecnologías utilizadas

- **Python** con **Flask** — framework web
- **SQLAlchemy** — ORM para la base de datos
- **MySQL** con **PyMySQL** — base de datos
- **Jinja2** — motor de templates HTML
- **Bootstrap 5** — estilos y diseño responsive
- **Werkzeug** — hasheo de contraseñas
- **python-dotenv** — manejo de variables de entorno
- **requests** — conexión con API-Football

---

## Requisitos previos

- Python 3.10 o superior
- MySQL instalado y corriendo
- Cuenta en [dashboard.api-football.com](https://dashboard.api-football.com)

---

## Instalación

### 1. Clonar el repositorio

https://github.com/antonellafernanadez-cmd/mundial2026-jugadores.git

---

### 2. Ingresar al repositorio
cd mundial2026-jugadores
code .

---


### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```


### 4. Crear la base de datos en MySQL
```sql
CREATE DATABASE nombre_de_tu_base_de_datos;
```

---

## Ejecución

### 1. Iniciar la aplicación (crea las tablas automáticamente)
```bash
python app.py
```

### 2. Cargar los datos desde la API (solo la primera vez)
Abrir una segunda terminal con el venv activado y correr:
```bash
python seed.py
```

### 3. Acceder a la aplicación

Para comenzar a utilizar la aplicación, abra en el navegador: [http://localhost:5000/login](http://127.0.0.1:5000/)
```

## Estructura del proyecto

```
Practicamundial2026/
├── models/
│   ├── db.py
│   ├── jugador.py
│   ├── seleccion.py
│   ├── estadistica.py
│   └── usuario.py
├── controllers/
│   ├── jugadores_controllers.py
│   ├── seleccion_controllers.py
│   ├── estadisticas_controllers.py
│   └── usuario_controllers.py
├── routes/
│   ├── routes_auth.py
│   ├── routes_usuario.py
│   ├── routes_jugadores.py
│   ├── routes_seleccion.py
│   └── routes_estadisticas.py
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── jugadores.html
│   ├── detalle_jugador.html
│   ├── formulario_jugador.html
│   ├── jugador_editar.html
│   ├── selecciones.html
│   ├── detalle_seleccion.html
│   ├── formulario_estadisticas.html
│   ├── usuarios.html
│   └── edit_usuarios.html
├── static/
│   └── css/
│       └── style.css
├── utils/
│   └── decorators.py
├── config/
│   └── config.py
├── app.py
├── seed.py
├── .env
├── .gitignore
└── requirements.txt
```

---

## Roles de usuario

| Rol | Permisos |
|-----|----------|
| **admin** | Ver, crear, editar y eliminar jugadores, selecciones y usuarios |
| **user** | Solo puede ver jugadores y selecciones |

---

## Funcionalidades

- Registro e inicio de sesión con contraseña hasheada
- CRUD completo de jugadores (solo admin)
- Visualización de selecciones y sus jugadores
- Gestión de estadísticas por jugador
- Carga automática de datos desde API-Football
- Diseño temático Mundial 2026 con Bootstrap

---
# Endpoints implementados
GET-POST /users/register: Permite registrar nuevos usuarios.
GET-POST /login: Permite iniciar una sesión.
GET /bienvenida: Pantalla post-login para usuarios autenticados.
GET /logout: Permite cerrar una sesión.
GET /jugadores/ver_jugadores: Permite visualizar todos los jugadores cargados en la base de datos.
GET /jugadores/detalle/: Permite obtener un jugador existente mediante su id.
GET /jugadores/crear: Hace posible acceder al formulario para añadir un nuevo jugador.
POST /jugadores/crear: Permite crear un nuevo jugador en la base de datos.
GET /jugadores/editar/: Permite al usuario administrador acceder al formulario para editar un jugador.
POST /jugadores/editar/: Permite actualizar los datos de un jugador existente.
GET /jugadores/eliminar/: Permite eliminar un jugador de la base de datos.
GET /estadisticas/<jugador_id>: Permite visualizar las estadísticas de un jugador específico.
GET /estadisticas/editar/<jugador_id>: Permite acceder al formulario para editar las estadísticas de un jugador.
POST /estadisticas/editar/<jugador_id>: Permite guardar las modificaciones de las estadísticas en la base de datos.
GET /selecciones/ver_selecciones: Permite visualizar el listado de todas las selecciones de fútbol.
GET /selecciones/: Permite obtener el detalle de una selección específica mediante su id.
GET /users/: Permite al administrador visualizar el listado completo de usuarios del sistema.
GET /users/update/: Permite acceder al formulario para editar los datos o rol de un usuario.
POST /users/update/: Permite guardar la edición de un usuario en la base de datos.
GET /users/delete/: Permite eliminar un usuario de la base de datos.
GET /users/aprobar/: Permite al administrador aprobar y activar un usuario que se encuentra pendiente.

## Autores
Antonella Fernandez, Leonel Bustos, Javier Cabrera y Marcelo Britos
Proyecto grupal — Programación II — 2026
