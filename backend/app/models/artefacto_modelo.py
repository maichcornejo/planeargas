from flask_sqlalchemy import SQLAlchemy

# Inicializar SQLAlchemy
db = SQLAlchemy()

class Artefacto(db.Model):
    __tablename__ = 'artefactos'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    orientacion = db.Column(db.String(50), nullable=False)
    imagen = db.Column(db.LargeBinary, nullable=False)  # Almacena la imagen en binario (BYTEA)

    def __init__(self, nombre, orientacion, imagen):
        self.nombre = nombre
        self.orientacion = orientacion
        self.imagen = imagen

    def __repr__(self):
        return f'<Artefacto {self.nombre}, {self.orientacion}>'
