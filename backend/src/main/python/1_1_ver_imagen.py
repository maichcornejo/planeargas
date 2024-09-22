from PIL import Image

def abrir_imagen_pillow(ruta_archivo):
    # Abrir la imagen
    imagen = Image.open(ruta_archivo)
    
    # Mostrar la imagen
    imagen.show()

# Ejemplo de uso
ruta_imagen_original = '/home/Maia/planeargas/backend/src/imagen_entrada/planta_1.png'
ruta_caneria = '/home/Maia/planeargas/backend/src/imagen_salida/caneria.png'
ruta_artefactos = '/home/Maia/planeargas/backend/src/imagen_salida/artefactos.png'
ruta_paredes = '/home/Maia/planeargas/backend/src/imagen_salida/paredes.png'
ruta_subidas_bajadas = '/home/Maia/planeargas/backend/src/imagen_salida/subidas_bajadas.png'
ruta_ventilaciones = '/home/Maia/planeargas/backend/src/imagen_salida/ventilaciones.png'
abrir_imagen_pillow(ruta_caneria)
abrir_imagen_pillow(ruta_artefactos)
abrir_imagen_pillow(ruta_paredes)
abrir_imagen_pillow(ruta_subidas_bajadas)
abrir_imagen_pillow(ruta_ventilaciones)
abrir_imagen_pillow(ruta_imagen_original)