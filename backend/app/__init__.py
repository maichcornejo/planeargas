from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

import os


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://PLA:PLA@database:5432/planeargas'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Configuración específica de CORS
    cors_origins = os.getenv('CORS_ORIGINS', '*').split(',')
    CORS(app, resources={
        r"/*": {
            "origins": cors_origins
        }
    })
    
    # Registrar blueprints
    from .routes.lote_routes import lote_bp
    app.register_blueprint(lote_bp)

    # Importar modelos después de inicializar db
    from app.models.lote_model import Lote
    
    @app.route('/')
    def home():
        return "¡Bienvenidos al backend de Planear Gas!"
    
    return app
