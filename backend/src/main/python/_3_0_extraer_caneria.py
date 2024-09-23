import rasterio
import math
import cv2
import numpy as np
from shapely.geometry import LineString, MultiLineString
from shapely.ops import unary_union
from shapely.affinity import affine_transform
import os

def leer_puntos_txt(ruta_archivo_subidas):
    puntos = []
    with open(ruta_archivo_subidas, 'r') as archivo:
        for linea in archivo:
            # Eliminar paréntesis y espacios, luego dividir por coma
            linea = linea.strip().replace('(', '').replace(')', '')
            x_str, y_str = linea.split(',')
            # Convertir las cadenas a floats y añadir como tupla (x, y)
            x, y = float(x_str), float(y_str)
            puntos.append((x, y))
    return puntos

def distancia_punto_recta(x, y ,xi, yi, xf, yf):

    # Calculamos el numerador de la fórmula
    numerador = abs((yf - yi) * x - (xf - xi) * y + xf * yi - yf * xi)
    
    # Calculamos el denominador de la fórmula
    denominador = math.sqrt((yf - yi)**2 + (xf - xi)**2)
    
    # Finalmente calculamos la distancia
    distancia = numerador / denominador
    return distancia

def process_geotiff_caneria(file_path, output_file):
    # Cargar el archivo GeoTIFF
    with rasterio.open(file_path) as src:
        # Leer la imagen y la transformación affine
        image = src.read(1)  # Leer la primera banda de la imagen
        transform = src.transform

    # Encontrar líneas usando Hough Transform
    lines = cv2.HoughLinesP(image, 1, np.pi / 180, threshold=10, minLineLength=10, maxLineGap=5)
    escala = 250
    subidas = leer_puntos_txt(ruta_archivo_subidas)
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
                print(x1, y1, x2, y2)
                
                punto = subidas[0]
                print(punto)
                print(distancia_punto_recta(punto[0], punto[1],x1, y1, x2, y2 ))
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
                        f.write(f'\\draw [color=red] ({x1:.2f}, {y1:.2f}) -- ({x2:.2f}, {y2:.2f});\n')
            else:
                coords = list(vector.coords)
                for i in range(len(coords) - 1):
                    x1, y1 = coords[i]
                    x2, y2 = coords[i + 1]
                    f.write(f'\\draw [color=red] ({x1:.2f}, {y1:.2f}) -- ({x2:.2f}, {y2:.2f});\n')


# Ruta al archivo GeoTIFF
file_path = '/home/meli/planeargas/backend/src/imagen_raster/caneria.tif'

# Ruta al archivo de salida
output_file = '/home/meli/planeargas/backend/src/txt_resultantes/resultados_caneria_latex.txt'

ruta_archivo_subidas = '/home/meli/planeargas/backend/src/txt_resultantes/resultados_subidas_bajadas.txt'
# Procesar el archivo GeoTIFF
process_geotiff_caneria(file_path, output_file)
