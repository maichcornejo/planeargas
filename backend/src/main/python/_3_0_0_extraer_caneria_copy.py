import rasterio
import math
import cv2
import re
import numpy as np
from shapely.geometry import LineString, MultiLineString
from shapely.ops import unary_union
from shapely.affinity import affine_transform
import os

# Leer los vectores del archivo de entrada
def leer_vectores(ruta_archivo):
    vectores = []
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Extraer coordenadas de los vectores
            coordenadas = re.findall(r"\(([\d.]+), ([\d.]+)\) -- \(([\d.]+), ([\d.]+)\)", linea)
            if coordenadas:
                x1, y1, x2, y2 = map(float, coordenadas[0])
                vectores.append(((x1, y1), (x2, y2)))
    return vectores

# Método para leer los puntos desde el archivo
def leer_puntos(ruta_archivo):
    puntos = []
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Usar expresión regular para extraer los puntos del formato LaTeX
            coordenadas = re.findall(r"\(([\d.]+), ([\d.]+)\)", linea)
            if coordenadas:
                for coord in coordenadas:
                    x, y = map(float, coord)
                    puntos.append((x, y))
    return puntos

# Función para calcular la distancia de un punto a un vector
def distancia_punto_vector(x, y, x1, y1, x2, y2):
    # Numerador de la fórmula
    numerador = abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1)
    # Denominador de la fórmula
    denominador = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
    # Calcular la distancia
    distancia = numerador / denominador
    return distancia

# Función para encontrar el vector más cercano a cada punto
def asignar_punto_a_vector(puntos, vectores):
    asignaciones = []

    for punto in puntos:
        x, y = punto
        distancia_minima = float('inf')
        vector_mas_cercano = None

        for vector in vectores:
            (x1, y1), (x2, y2) = vector
            # Calcular la distancia del punto al vector
            distancia = distancia_punto_vector(x, y, x1, y1, x2, y2)
            
            # Si la distancia es menor que la distancia mínima actual, actualizamos
            if distancia < distancia_minima:
                distancia_minima = distancia
                vector_mas_cercano = vector

        # Guardamos la asignación del punto al vector más cercano
        asignaciones.append((punto, vector_mas_cercano, distancia_minima))

    return asignaciones

def process_geotiff_caneria(file_path, output_file, color):
    # Cargar el archivo GeoTIFF
    with rasterio.open(file_path) as src:
        # Leer la imagen y la transformación affine
        image = src.read(1)  # Leer la primera banda de la imagen
        transform = src.transform

    # Encontrar líneas usando Hough Transform
    lines = cv2.HoughLinesP(image, 1, np.pi / 180, threshold=10, minLineLength=10, maxLineGap=5)
    escala = 250
    # Convertir líneas a formato LineString de Shapely
    vectors = []
    if lines is not None:
        raw_lines = []
        for line in lines:
            for x1, y1, x2, y2 in line:
                # Dividir las coordenadas para ajustar la escala
                start = (x1 / escala, y1 / escala)
                end = (x2 / escala, y2 / escala)
                line_string = LineString([start, end])
                raw_lines.append(line_string)
        # Merge similar lines
        vectors = raw_lines

    
    

    # Exportar a archivo txt con formato LaTeX
    with open(output_file, 'w') as f:
        for vector in vectors:
            if isinstance(vector, MultiLineString):
                for line in vector:
                    coords = list(line.coords)
                    for i in range(len(coords) - 1):
                        x1, y1 = coords[i]
                        x2, y2 = coords[i + 1]
                        f.write(f'\\draw [color={color}] ({-x1:.2f}, {-y1:.2f}) -- ({-x2:.2f}, {-y2:.2f});\n')
            else:
                coords = list(vector.coords)
                for i in range(len(coords) - 1):
                    x1, y1 = coords[i]
                    x2, y2 = coords[i + 1]
                    f.write(f'\\draw [color={color}] ({-x1:.2f}, {-y1:.2f}) -- ({-x2:.2f}, {-y2:.2f});\n')

# Ruta al archivo GeoTIFF
file_path = '/home/meli/planeargas/backend/src/imagen_raster/caneria.tif'
color = 'red'
# Ruta al archivo de salida
output_file = '/home/meli/planeargas/backend/src/txt_resultantes/resultados_caneria_latex.txt'
ruta_entrada_saltos = "/home/meli/planeargas/backend/src/txt_resultantes/resultados_subidas_bajadas.txt"
# Procesar el archivo GeoTIFF
process_geotiff_caneria(file_path, output_file, color)
vectores = leer_vectores(output_file)
subidas = leer_puntos(ruta_entrada_saltos)
asignaciones = asignar_punto_a_vector(subidas, vectores)
# Mostrar los resultados
for asignacion in asignaciones:
    punto, vector, distancia = asignacion
    print(f"El punto {punto} está más cerca del vector {vector} con una distancia de {distancia:.2f}")