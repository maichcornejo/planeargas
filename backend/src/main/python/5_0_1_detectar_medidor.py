import cv2
import numpy as np
import os

def encontrar_medidor_por_ubicacion_fija(image, ancho_medidor=0.40, alto_medidor=0.30, resolucion=15.65, tolerancia=20):
    # Proporción en píxeles para la escala del plano
    height, width, _ = image.shape
    metros_a_pixeles = width / resolucion  # Resolución horizontal (metros en la parte inferior)

    # Dimensiones del medidor en píxeles
    ancho_medidor_px = int(ancho_medidor * metros_a_pixeles)
    alto_medidor_px = int(alto_medidor * metros_a_pixeles)

    # Limitar la búsqueda a la parte más inferior del plano (últimos 10% de la imagen)
    y_inferior = int(height * 0.90)
    sub_image = image[y_inferior:, :]

    # Convertir la imagen a escala de grises y aplicar detección de bordes
    gray = cv2.cvtColor(sub_image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 50, 150)

    # Encontrar contornos
    contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Buscar el primer rectángulo desde la esquina inferior izquierda que coincida con las dimensiones del medidor
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        # Comprobamos si las dimensiones coinciden con las del medidor (aumentamos la tolerancia)
        if (ancho_medidor_px - tolerancia) <= w <= (ancho_medidor_px + tolerancia) and (alto_medidor_px - tolerancia) <= h <= (alto_medidor_px + tolerancia):
            # Coordenada absoluta en la imagen completa
            x_abs = x
            y_abs = y + y_inferior

            # Crear una nueva imagen que contenga solo el medidor
            medidor = image[y_abs:y_abs+h, x_abs:x_abs+w]
            
            # Crear una imagen en blanco (transparente) para el fondo
            medidor_sin_fondo = np.zeros_like(image)
            medidor_sin_fondo[y_abs:y_abs+h, x_abs:x_abs+w] = image[y_abs:y_abs+h, x_abs:x_abs+w]

            # Guardar la imagen del medidor sin fondo
            cv2.imwrite('/home/Maia/planeargas/backend/src/detecciones/medidor_sin_fondo.png', medidor_sin_fondo)

            # Retornar las coordenadas y dimensiones del medidor
            return (x_abs, y_abs, w, h)
    
    return None  # Si no se encuentra el medidor

# Verificar si la imagen se carga correctamente
image_path = '/home/Maia/planeargas/backend/src/imagen_entrada/planta_1.png'
if os.path.exists(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: No se pudo cargar la imagen en {image_path}. Verifica el archivo y la ruta.")
    else:
        # Ejecutar la función para encontrar el medidor por ubicación fija
        medidor_coordenadas = encontrar_medidor_por_ubicacion_fija(image)

        if medidor_coordenadas:
            x_abs, y_abs, w, h = medidor_coordenadas
            print(f"Medidor encontrado en las coordenadas (x, y): ({x_abs}, {y_abs}) con ancho: {w} y alto: {h} píxeles")
        else:
            print("Medidor no encontrado")
else:
    print(f"Error: La ruta {image_path} no existe. Verifica si el archivo está en la ubicación correcta.")
