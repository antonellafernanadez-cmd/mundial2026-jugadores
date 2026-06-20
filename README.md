# mundial2026-jugadores
Aplicación web mundial 2026 - Parte Jugadores
# Mundial 2026 - Gestión de Jugadores

Aplicación web desarrollada con Flask para gestionar jugadores del Mundial 2026. Permite visualizar selecciones, jugadores y estadísticas, con sistema de autenticación y roles de usuario.

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
```bash
git clone <url-del-repositorio>
cd Practicamundial2026
```

### 2. Crear y activar el entorno virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
Crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:
```
MYSQL_USER=tu_usuario
MYSQL_PASSWORD=tu_contraseña
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=nombre_de_tu_base_de_datos
API_FOOTBALL_KEY=tu_api_key
```

### 5. Crear la base de datos en MySQL
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
Abrir el navegador en:
```
http://127.0.0.1:5000
```

---

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

## Autores
Antonella Fernandez, Leonel Bustos, Javier Cabrera y Marcelo Britos
Proyecto grupal — Programación II — 2026
