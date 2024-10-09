from app import db
from app.models.plano_model import Plano
import os

def crear_plano(data, credencial_file=None, planta_file=None):
    # Procesar los archivos adjuntos
    credencial_path = None
    planta_path = None

    if credencial_file:
        credencial_path = guardar_archivo(credencial_file, 'uploads/credenciales')
    
    if planta_file:
        planta_path = guardar_archivo(planta_file, 'uploads/plantas')

    # Crear el nuevo plano
    nuevo_plano = Plano(
        artefactos=data.get('artefactos'),
        material=data.get('material'),
        nombre=data.get('nombre'),
        apellido=data.get('apellido'),
        matricula=data.get('matricula'),
        categoria=data.get('categoria'),
        credencial_path=credencial_path,
        planta_path=planta_path
    )

    # Guardar en la base de datos
    db.session.add(nuevo_plano)
    db.session.commit()

    return nuevo_plano

def guardar_archivo(archivo, carpeta):
    # Crear la carpeta si no existe
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    
    # Definir la ruta completa del archivo
    archivo_path = os.path.join(carpeta, archivo.filename)
    
    # Guardar el archivo en la ruta especificada
    archivo.save(archivo_path)
    
    return archivo_path
