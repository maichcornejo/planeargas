from flask import Flask
from app.models.artefacto_modelo import db
from app.models.cargar_artefactos import cargar_imagenes_a_db

app = Flask(__name__)

# Configuración de la base de datos con el puerto 28001
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://PLA:PLA@localhost:28001/planeargas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

@app.route('/')
def home():
    return "¡Bienvenidos al backend de Planear Gas!"

# Ruta para cargar las imágenes a la base de datos
@app.route('/cargar_imagenes')
def cargar_imagenes():
    with app.app_context():
        cargar_imagenes_a_db()
    return "Imágenes cargadas exitosamente."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
