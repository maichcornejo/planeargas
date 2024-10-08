from flask import Flask
from .artefacto_modelo import db
from .cargar_artefactos import cargar_imagenes_a_db

def create_app():
    app = Flask(__name__)
# Configuración de la base de datos con el puerto 28001
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://PLA:PLA@localhost:28001/planeargas'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    return app

app = create_app()

with app.app_context():
    cargar_imagenes_a_db()  # Llama a la función que carga las imágenes
