import cv2
import numpy as np
import os

def encontrar_medidor_por_ubicacion_fija(image, resolucion):
    ancho_medidor=0.40
    alto_medidor=0.30
    tolerancia=20
    height, width, _ = image.shape
    metros_a_pixeles = width / resolucion  # Resolución horizontal (metros en la parte inferior)

    # Dimensiones del medidor en píxeles
    ancho_medidor_px = int(ancho_medidor * metros_a_pixeles)
    alto_medidor_px = int(alto_medidor * metros_a_pixeles)

    # Solo uso el 10% inferior de la imagen 
    y_inferior = int(height * 0.90)
    sub_image = image[y_inferior:, :]
    gray = cv2.cvtColor(sub_image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 50, 150)
    contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Buscar el primer rectángulo desde la esquina inferior izquierda que coincida con las dimensiones del medidor
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if (ancho_medidor_px - tolerancia) <= w <= (ancho_medidor_px + tolerancia) and (alto_medidor_px - tolerancia) <= h <= (alto_medidor_px + tolerancia):
            x_abs = x
            y_abs = y + y_inferior

            # Crear una nueva imagen que contenga solo el medidor
            medidor_sin_fondo = np.zeros_like(image)
            medidor_sin_fondo[y_abs:y_abs+h, x_abs:x_abs+w] = image[y_abs:y_abs+h, x_abs:x_abs+w]

            # Guardar la imagen del medidor sin fondo
            cv2.imwrite('/home/meli/planeargas/backend/src/detecciones/medidor_sin_fondo.png', medidor_sin_fondo)

            # Retornar las coordenadas y dimensiones del medidor
            return (x_abs, y_abs, w, h)
    
    return None  

def guardar_ubicacion_txt(x_abs, y_abs, w, h, output_txt_path):
   # Cargo el txt con la info del medidor
    with open(output_txt_path, 'w') as file:
        file.write(f"Coordenadas del medidor de gas:\n")
        file.write(f"Posición X: {x_abs} píxeles\n")
        file.write(f"Posición Y: {y_abs} píxeles\n")
        file.write(f"Ancho del medidor: {w} píxeles\n")
        file.write(f"Alto del medidor: {h} píxeles\n")
    print(f"Ubicación guardada en {output_txt_path}")


def proceso_principal_medidor(image_path, resolucion):
    if os.path.exists(image_path):
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: No se pudo cargar la imagen en {image_path}. Verifica el archivo y la ruta.")
        else:
            # Ejecutar la función para encontrar el medidor
            medidor_coordenadas = encontrar_medidor_por_ubicacion_fija(image,resolucion)

            if medidor_coordenadas:
                x_abs, y_abs, w, h = medidor_coordenadas
                print(f"Medidor encontrado en las coordenadas (x, y): ({x_abs}, {y_abs}) con ancho: {w} y alto: {h} píxeles")
                output_txt_path = '/home/meli/planeargas/backend/src/detecciones/ubicacion_medidor.txt'
                guardar_ubicacion_txt(x_abs, y_abs, w, h, output_txt_path)
            else:
                print("Medidor no encontrado")
    else:
        print(f"Error: La ruta {image_path} no existe. Verifica si el archivo está en la ubicación correcta.")

ruta = '/home/meli/planeargas/backend/src/imagen_entrada/planta_1.png'
resolucion = 15.65
proceso_principal_medidor(ruta,resolucion)