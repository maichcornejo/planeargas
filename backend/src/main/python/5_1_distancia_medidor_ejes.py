import cv2
import numpy as np
import os

# Función para encontrar el medidor de gas por ubicación fija
def encontrar_medidor_por_ubicacion_fija(image, ancho_medidor=0.40, alto_medidor=0.30, resolucion=15.65, tolerancia=20):
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

    # Buscar el primer rectángulo que coincida con las dimensiones del medidor
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if (ancho_medidor_px - tolerancia) <= w <= (ancho_medidor_px + tolerancia) and (alto_medidor_px - tolerancia) <= h <= (alto_medidor_px + tolerancia):
            x_abs = x
            y_abs = y + y_inferior
            return (x_abs, y_abs, w, h)  # Retorna coordenadas y dimensiones del medidor
    return None

# Cargar la imagen
image_path = '/home/Maia/planeargas/backend/src/imagen_salida/paredes.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
image_color = cv2.imread(image_path)  # Cargar también la imagen a color para dibujar

# Detectar bordes y líneas
_, thresh = cv2.threshold(image, 240, 255, cv2.THRESH_BINARY_INV)
edges = cv2.Canny(thresh, 50, 150, apertureSize=3)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=50, maxLineGap=5)

# Variables para ejes medianeros
left_medianero_x = float('inf')
right_medianero_x = -float('inf')
municipal_line_y = None

# Encontrar los ejes medianeros
for line in lines:
    x1, y1, x2, y2 = line[0]
    if abs(x1 - x2) < 10:  # Línea vertical
        if x1 < left_medianero_x:
            left_medianero_x = x1
        if x1 > right_medianero_x:
            right_medianero_x = x1
    if abs(y1 - y2) < 10:  # Línea horizontal (línea municipal)
        if municipal_line_y is None or y1 > municipal_line_y:
            municipal_line_y = y1

# Calcular la longitud de la línea municipal en píxeles
longitud_municipal_pixels = right_medianero_x - left_medianero_x

# Calcular la escala de metros por píxel
longitud_real_metros = 15.65  # Se refiere al plano de referencia
escala_metros_por_pixel = longitud_real_metros / longitud_municipal_pixels

# Encontrar el medidor en la imagen original
medidor_coordenadas = encontrar_medidor_por_ubicacion_fija(image_color)

if medidor_coordenadas:
    x_abs, y_abs, w, h = medidor_coordenadas
    centro_medidor_x = x_abs + w // 2  # Coordenada del centro del medidor en x

    # Calcular distancias del medidor a los ejes medianeros
    distancia_izquierda_px = abs(centro_medidor_x - left_medianero_x)
    distancia_derecha_px = abs(centro_medidor_x - right_medianero_x)

    # Convertir las distancias a metros
    distancia_izquierda_metros = distancia_izquierda_px * escala_metros_por_pixel
    distancia_derecha_metros = distancia_derecha_px * escala_metros_por_pixel

    # Guardar los resultados en un archivo .txt
    txt_output_path = '/home/Maia/planeargas/backend/src/detecciones/distancia_medidor_ejes.txt'
    with open(txt_output_path, 'w') as f:
        f.write(f'Eje Medianero Izquierdo (X): {left_medianero_x} píxeles\n')
        f.write(f'Eje Medianero Derecho (X): {right_medianero_x} píxeles\n')
        f.write(f'Longitud del Eje Municipal en Píxeles: {longitud_municipal_pixels} píxeles\n')
        f.write(f'Longitud del Eje Municipal en Metros: {longitud_real_metros:.2f} m\n')
        f.write(f'Distancia desde el Medidor al Eje Izquierdo: {distancia_izquierda_metros:.2f} m\n')
        f.write(f'Distancia desde el Medidor al Eje Derecho: {distancia_derecha_metros:.2f} m\n')

    print(f"Archivo generado: {txt_output_path}")

    # Crear una imagen visualizando el medidor y las distancias (opcional)
    cv2.line(image_color, (centro_medidor_x, municipal_line_y), (left_medianero_x, municipal_line_y), (0, 255, 0), 2)  # Línea verde al eje izquierdo
    cv2.line(image_color, (centro_medidor_x, municipal_line_y), (right_medianero_x, municipal_line_y), (0, 0, 255), 2)  # Línea roja al eje derecho
    cv2.circle(image_color, (centro_medidor_x, y_abs + h // 2), 5, (255, 0, 0), -1)  # Marcar el centro del medidor en azul

    # Guardar la imagen visual
    output_image_path = '/home/Maia/planeargas/backend/src/detecciones/distancia_medidor_visual.png'
    cv2.imwrite(output_image_path, image_color)
    print(f"Imagen con las distancias generada: {output_image_path}")
else:
    print("No se pudo encontrar el medidor en la imagen.")
