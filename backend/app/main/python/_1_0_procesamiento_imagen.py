import cv2
import numpy as np
import os

def procesar_imagen(input_image_path, output_directory):
    # Verificar si la imagen de entrada es válida
    image = cv2.imread(input_image_path)
    if image is None:
        raise ValueError(f"No se pudo cargar la imagen en {input_image_path}. Verifica el archivo y la ruta.")

    # Convertir la imagen a formato RGB
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
        'artefactos': [128, 128, 128],  # Gris
        'cotas': [  0,   0, 255] #Azul
    }

    # Crear máscaras para cada color
    masks = {}
    for label, color in color_mapping.items():
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

        # Cambiar los píxeles negros (fondo) a blanco
        if label == 'paredes':
            output_image[mask == 0] = [255, 255, 255]  # Fondo blanco

        # Guardar la imagen resultante
        cv2.imwrite(os.path.join(output_directory, f'{label}.png'), cv2.cvtColor(output_image, cv2.COLOR_RGB2BGR))

if __name__ == "__main__":
    # Rutas de entrada y salida
    entrada_image_path = '/home/Maia/planeargas/backend/app/imagen_entrada/planta_1.png'
    salida_directory = '/home/Maia/planeargas/backend/app/imagen_salida/'
    
    # Ejecutar el procesamiento
    procesar_imagen(entrada_image_path, salida_directory)
