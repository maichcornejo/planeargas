import rasterio
import cv2
import numpy as np
from shapely.geometry import LineString, MultiLineString
from shapely.ops import unary_union
from shapely.affinity import affine_transform
import os

def process_geotiff_caneria(file_path, output_file):
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

# Procesar el archivo GeoTIFF
process_geotiff_caneria(file_path, output_file)
