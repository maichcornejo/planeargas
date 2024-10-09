from app import db

class Plano(db.Model):
    __tablename__ = 'planos'

    id = db.Column(db.Integer, primary_key=True)
    artefactos = db.Column(db.Integer, nullable=False)
    material = db.Column(db.String(100), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    credencial_path = db.Column(db.String(200))
    planta_path = db.Column(db.String(200))
