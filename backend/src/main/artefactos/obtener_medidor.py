"""
This module contains functions and classes to obtain and process meter data using Rasterio.
"""


import rasterio
import numpy as np
import cv2
import os

def process_geotiff(image_path, output_txt):
    # Cargar la imagen GeoTIFF
    with rasterio.open(image_path) as dataset:
        image = dataset.read(1)  # Leer la primera (y única) banda
        transform = dataset.transform  # Obtener la transformación geo-espacial

    # Normalizar la imagen para mejorar la detección de bordes
    image_normalized = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    
    # Aplicar un filtro de desenfoque para reducir el ruido
    image_blurred = cv2.GaussianBlur(image_normalized, (5, 5), 0)

    # Detectar bordes usando Canny
    edges = cv2.Canny(image_blurred, 50, 150)

    # Encontrar contornos en la imagen
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Filtrar contornos para encontrar un rectángulo con dimensiones aproximadas 0.40m x 0.30m
    medidor_contour = None
    for contour in contours:
        # Aproximar al rectángulo
        epsilon = 0.05 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        if len(approx) == 4:  # Asegurarse de que sea un cuadrilátero
            # Obtener las dimensiones del rectángulo aproximado
            x, y, w, h = cv2.boundingRect(approx)
            # Convertir dimensiones a unidades geoespaciales
            width_geo = w * transform[0]  # Tamaño del píxel
            height_geo = h * transform[4]  # Tamaño del píxel

            # Chequear si las dimensiones están cerca de 0.40m x 0.30m
            if np.isclose(width_geo, 0.40, atol=0.1) and np.isclose(height_geo, 0.30, atol=0.1):
                medidor_contour = approx
                break

    if medidor_contour is None:
        raise ValueError("No se encontró un medidor con las dimensiones especificadas.")

    # Calcular las coordenadas del centro del medidor
    M = cv2.moments(medidor_contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
    else:
        cx, cy = 0, 0

    # Convertir las coordenadas del píxel a coordenadas geográficas
    coords_x = transform[2] + cx * transform[0]
    coords_y = transform[5] + cy * transform[4]

    # Calcular distancias a los ejes medianeros (esto depende de la información geográfica)
    # Aquí se suponen distancias arbitrarias, debes ajustar según tu contexto
    distancia_x = abs(coords_x)  # Distancia al eje X (ejemplo)
    distancia_y = abs(coords_y)  # Distancia al eje Y (ejemplo)

    # Generar el archivo TXT
    with open(output_txt, 'w') as f:
        f.write(f"Coordenadas del medidor:\n")
        f.write(f"X: {coords_x:.3f}, Y: {coords_y:.3f}\n")
        f.write(f"Distancia al eje medianero X: {distancia_x:.3f} m\n")
        f.write(f"Distancia al eje medianero Y: {distancia_y:.3f} m\n")

# Ejecución del servicio
image_path = 'ruta/al/archivo_geotiff.tif'
output_txt = 'ruta/al/archivo_salida.txt'

process_geotiff(image_path, output_txt)
