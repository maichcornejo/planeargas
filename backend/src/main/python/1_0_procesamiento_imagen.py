import cv2
import numpy as np
import os
import psycopg2

def insertar_plano(nombre_plano):
    """
    Inserta un nuevo plano si no existe en la tabla planos.
    """
    conn = psycopg2.connect(
        dbname="labprog", 
        user="APP", 
        password="APP", 
        host="localhost",
        port="28001"  # Agrega el puerto correcto
    )
    cur = conn.cursor()

    # Verificar si el plano ya existe
    cur.execute("SELECT id FROM planos WHERE nombre_plano = %s", (nombre_plano,))
    result = cur.fetchone()

    if result is None:
        # Si no existe, insertarlo
        cur.execute(
            "INSERT INTO planos (nombre_plano) VALUES (%s) RETURNING id", (nombre_plano,)
        )
        plano_id = cur.fetchone()[0]
    else:
        # Si ya existe, obtener su ID
        plano_id = result[0]

    conn.commit()
    cur.close()
    conn.close()

    return plano_id

# Ruta de la imagen de entrada y las imágenes de salida
input_image_path = '/home/Maia/planeargas/backend/src/imagen_entrada/planta_2.png'
output_directory = '/home/Maia/planeargas/backend/src/imagen_salida/'

# Nombre del plano (puedes extraerlo del nombre del archivo, por ejemplo)
nombre_plano = os.path.basename(input_image_path).split('.')[0]

# Guardar el plano en la base de datos
plano_id = insertar_plano(nombre_plano)
print(f"Plano '{nombre_plano}' guardado en la base de datos con ID {plano_id}.")

# Verificar si la imagen de entrada es válida
image = cv2.imread(input_image_path)
if image is None:
    raise ValueError(f"No se pudo cargar la imagen en {input_image_path}. Verifica el archivo y la ruta.")

# Convertir la imagen a formato RGB si es necesario (OpenCV carga en BGR por defecto)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Obtener los colores únicos en la imagen
unique_colors = np.unique(image_rgb.reshape(-1, image_rgb.shape[2]), axis=0)
print("Colores únicos detectados:", unique_colors)

# Definir los colores específicos (en RGB)
color_mapping = {
    'caneria': [255, 0, 0],         # Rojo
    'subidas_bajadas': [255, 63, 0], # Rojo más claro
    'ventilaciones': [0, 255, 0],   # Verde
    'paredes': [0, 0, 0],      # Negro
    'artefactos': [128, 128, 128]  # Gris
}

# Crear máscaras para cada color
masks = {}
for label, color in color_mapping.items():
    # Crear la máscara para el color actual
    mask = cv2.inRange(image_rgb, np.array(color), np.array(color))
    masks[label] = mask

# Eliminar las imágenes existentes en la ruta de salida
for filename in os.listdir(output_directory):
    file_path = os.path.join(output_directory, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)

for label, mask in masks.items():
    # Crear una imagen vacía con el mismo tamaño
    output_image = np.zeros_like(image_rgb)

    # Aplicar la máscara para el color específico
    output_image[mask != 0] = color_mapping[label]

    # Si es la máscara de las paredes (color negro), cambia el negro a blanco
    if label == 'paredes' :
        # Cambiar todos los píxeles negros (fondo) a blanco
        output_image[mask == 0] = [255, 255, 255]  # Fondo blanco para los píxeles que no son paredes

    # Guardar la imagen resultante
    cv2.imwrite(os.path.join(output_directory, f'{label}.png'), cv2.cvtColor(output_image, cv2.COLOR_RGB2BGR))
