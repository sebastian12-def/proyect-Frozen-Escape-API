# Frozen Escape API ❄️

API REST desarrollada con Django REST Framework que simula un juego de supervivencia en condiciones extremas de frío.

## 🎮 Descripción del juego
El jugador debe gestionar su temperatura y energía para sobrevivir en un entorno congelado.  
Cada acción afecta su estado y existe un componente aleatorio que puede cambiar el resultado.

## 🧱 Tecnologías
- Python
- Django
- Django REST Framework
- SQLite

## 📊 Modelo de datos
- Usuario
- EstadoJugador (relación 1 a 1)
- Accion

## 🔗 Endpoints

### Crear usuario
POST /api/usuarios/

### Consultar estado
GET /api/estado/{id}

### Ejecutar acción
POST /api/accion/

### Ranking
GET /api/ranking/

## ⚙️ Ejecución

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver