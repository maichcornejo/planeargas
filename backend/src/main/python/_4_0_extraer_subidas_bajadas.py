import rasterio
import cv2
import numpy as np

def process_geotiff_puntos(file_path, output_file, color):
    # Cargar el archivo GeoTIFF
    with rasterio.open(file_path) as src:
        # Leer la imagen y la transformación affine
        image = src.read(1)  # Leer la primera banda de la imagen

    # Aplicar un umbral para detectar puntos en la imagen
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # Encontrar los contornos de los puntos
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    escala = 250
    puntos = []

    # Extraer los puntos clave (centroides de los contornos)
    for contour in contours:
        M = cv2.moments(contour)
        if M['m00'] != 0:
            cx = M['m10'] / M['m00']  # Coordenada X del centroide
            cy = M['m01'] / M['m00']  # Coordenada Y del centroide
            puntos.append((cx / escala, cy / escala))

    # Exportar puntos a archivo txt en formato LaTeX para TikZ
    with open(output_file, 'w') as f:
        for x, y in puntos:
            f.write(f'\\fill [color={color}] ({x:.2f}, {y:.2f}) circle (1pt);\n')

# Ruta al archivo GeoTIFF de puntos
file_path = '/home/Maia/planeargas/backend/src/imagen_raster/subidas_bajadas.tif'
color = 'blue'
# Ruta al archivo de salida
output_file = '/home/Maia/planeargas/backend/src/txt_resultantes/resultados_subidas_bajadas.txt'

# Procesar el archivo GeoTIFF para extraer puntos
process_geotiff_puntos(file_path, output_file, color)

