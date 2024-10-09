from app import db

class Lote(db.Model):

    __tablename__ = 'lote'  # Nombre de la tabla

    id = db.Column(db.Integer, primary_key=True)
    tipo_calle = db.Column(db.String(50))
    nombre_calle = db.Column(db.String(100))
    altura = db.Column(db.Integer)
    manzana = db.Column(db.String(10))
    lote = db.Column(db.String(10))
    piso = db.Column(db.String(10))
    departamento = db.Column(db.String(10))
    entre_calles_1 = db.Column(db.String(100))
    entre_calles_2 = db.Column(db.String(100))
    distancia_esquinas = db.Column(db.Float)

    def to_dict(self):
        return {
            'id': self.id,
            'tipo_calle': self.tipo_calle,
            'nombre_calle': self.nombre_calle,
            'altura': self.altura,
            'manzana': self.manzana,
            'lote': self.lote,
            'piso': self.piso,
            'departamento': self.departamento,
            'entre_calles_1': self.entre_calles_1,
            'entre_calles_2': self.entre_calles_2,
            'distancia_esquinas': self.distancia_esquinas
        }
