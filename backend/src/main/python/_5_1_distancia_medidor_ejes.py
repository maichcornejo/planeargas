import cv2
import numpy as np
import os

def encontrar_medidor_por_ubicacion_fija(image, ancho_medidor=0.40, alto_medidor=0.30, resolucion=15.65, tolerancia=20):
    height, width, _ = image.shape
    metros_a_pixeles = width / resolucion  

    ancho_medidor_px = int(ancho_medidor * metros_a_pixeles)
    alto_medidor_px = int(alto_medidor * metros_a_pixeles)

    # solo uso el 10% de la imagen
    y_inferior = int(height * 0.90)
    sub_image = image[y_inferior:, :]

    gray = cv2.cvtColor(sub_image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 50, 150)

    contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if (ancho_medidor_px - tolerancia) <= w <= (ancho_medidor_px + tolerancia) and (alto_medidor_px - tolerancia) <= h <= (alto_medidor_px + tolerancia):
            x_abs = x
            y_abs = y + y_inferior
            return (x_abs, y_abs, w, h)  # Retorna las coordenadas y dimensiones del medidor
    return None

def proceso_distancia_medidor(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image_color = cv2.imread(image_path)  

    _, thresh = cv2.threshold(image, 240, 255, cv2.THRESH_BINARY_INV)
    edges = cv2.Canny(thresh, 50, 150, apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=50, maxLineGap=5)

    if lines is None:
        print("No se encontraron líneas en la imagen.")
        return

    medianero_izquierdo_x = float('inf')
    medianero_derecho_x = -float('inf')
    municipal_line_y = None

    for line in lines:
        x1, y1, x2, y2 = line[0]
        if abs(x1 - x2) < 10:  # Línea vertical
            if x1 < medianero_izquierdo_x:
                medianero_izquierdo_x = x1
            if x1 > medianero_derecho_x:
                medianero_derecho_x = x1
        if abs(y1 - y2) < 10:  # Línea horizontal
            if municipal_line_y is None or y1 > municipal_line_y:
                municipal_line_y = y1

    longitud_municipal_pixels = medianero_derecho_x - medianero_izquierdo_x
    longitud_real_metros = 15.65  
    escala_metros_por_pixel = longitud_real_metros / longitud_municipal_pixels

    medidor_coordenadas = encontrar_medidor_por_ubicacion_fija(image_color)

    if medidor_coordenadas:
        x_abs, y_abs, w, h = medidor_coordenadas
        centro_medidor_x = x_abs + w // 2  

        distancia_izquierda_px = abs(centro_medidor_x - medianero_izquierdo_x)
        distancia_derecha_px = abs(centro_medidor_x - medianero_derecho_x)

        distancia_izquierda_metros = distancia_izquierda_px * escala_metros_por_pixel
        distancia_derecha_metros = distancia_derecha_px * escala_metros_por_pixel

        txt_output_path = '/home/meli/planeargas/backend/src/detecciones/distancia_medidor_ejes.txt'
        with open(txt_output_path, 'w') as f:
            f.write(f'Eje Medianero Izquierdo (X): {medianero_izquierdo_x} píxeles\n')
            f.write(f'Eje Medianero Derecho (X): {medianero_derecho_x} píxeles\n')
            f.write(f'Longitud del Eje Municipal en Píxeles: {longitud_municipal_pixels} píxeles\n')
            f.write(f'Longitud del Eje Municipal en Metros: {longitud_real_metros:.2f} m\n')
            f.write(f'Distancia desde el Medidor al Eje Izquierdo: {distancia_izquierda_metros:.2f} m\n')
            f.write(f'Distancia desde el Medidor al Eje Derecho: {distancia_derecha_metros:.2f} m\n')

        print(f"Archivo generado: {txt_output_path}")

        cv2.line(image_color, (centro_medidor_x, municipal_line_y), (medianero_izquierdo_x, municipal_line_y), (0, 255, 0), 2) 
        cv2.line(image_color, (centro_medidor_x, municipal_line_y), (medianero_derecho_x, municipal_line_y), (0, 0, 255), 2)  
        cv2.circle(image_color, (centro_medidor_x, y_abs + h // 2), 5, (255, 0, 0), -1) 

        output_image_path = '/home/meli/planeargas/backend/src/detecciones/distancia_medidor_visual.png'
        cv2.imwrite(output_image_path, image_color)
        print(f"Imagen con las distancias generada: {output_image_path}")
    else:
        print("No se pudo encontrar el medidor en la imagen.")

imagen_detectar_ejes_medianeros = '/home/meli/planeargas/backend/src/imagen_salida/paredes.png'
proceso_distancia_medidor(imagen_detectar_ejes_medianeros)
