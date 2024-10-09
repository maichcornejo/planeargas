def crear_lote(data):
    from app import db  # Importa db dentro de la función para evitar importación circular
    from app.models.lote_model import Lote  # Importar el modelo dentro de la función
    
    nuevo_lote = Lote(
        tipo_calle=data.get('tipo_calle'),
        nombre_calle=data.get('nombre_calle'),
        altura=data.get('altura'),
        manzana=data.get('manzana'),
        lote=data.get('lote'),
        piso=data.get('piso'),
        departamento=data.get('departamento'),
        entre_calles_1=data.get('entre_calles_1'),
        entre_calles_2=data.get('entre_calles_2'),
        distancia_esquinas=data.get('distancia_esquinas')
    )
    db.session.add(nuevo_lote)
    db.session.commit()
    return nuevo_lote

def obtener_lote(calle, altura):
    from app import db  # Importa db dentro de la función
    from app.models.lote_model import Lote  # Importar el modelo dentro de la función
    
    return Lote.query.filter_by(nombre_calle=calle, altura=altura).first()
