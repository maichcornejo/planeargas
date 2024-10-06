import os
from .artefacto_modelo import Artefacto, db

# Ruta base relativa donde están las imágenes de los artefactos
BASE_DIR = os.path.join('backend', 'app', 'models', 'artefactos')

# Recorrer los directorios y cargar las imágenes en la base de datos
def cargar_imagenes_a_db():
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith('.png'):
                # Obtener nombre del artefacto y orientación
                artefacto_dir = os.path.basename(root)

                # Dividir el nombre del archivo en tres partes: numeroRandom, nombre del artefacto y orientación
                partes = file.split('_')
                if len(partes) == 3:
                    artefacto_nombre = partes[1]      # Nombre del artefacto es la segunda parte
                    orientacion = partes[2].replace('.png', '')  # La orientación es la tercera parte, sin ".png"
                else:
                    print(f"El archivo {file} no sigue el formato esperado.")
                    continue  # Saltar archivos que no siguen el formato esperado

                # Construir la ruta relativa del archivo
                ruta_imagen = os.path.join(root, file)
                
                # Leer el archivo como binario
                with open(ruta_imagen, 'rb') as f:
                    imagen_binaria = f.read()
                
                # Crear un nuevo registro de Artefacto
                nuevo_artefacto = Artefacto(nombre=artefacto_nombre, orientacion=orientacion, imagen=imagen_binaria)

                # Insertar en la base de datos
                db.session.add(nuevo_artefacto)
                db.session.commit()

                print(f"Artefacto {artefacto_nombre} con orientación {orientacion} cargado en la base de datos.")
