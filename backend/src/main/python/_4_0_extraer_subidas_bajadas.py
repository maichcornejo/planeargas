import rasterio
import cv2
import numpy as np
from rasterio.features import shapes
from shapely.geometry import shape
from math import sqrt

# Función para calcular la distancia entre dos puntos
def distancia(punto1, punto2):
    return sqrt((punto1[0] - punto2[0])**2 + (punto1[1] - punto2[1])**2)

def process_geotiff_puntos(file_path, output_file, color):
    # Cargar el archivo GeoTIFF
    with rasterio.open(file_path) as src:
        # Leer la imagen y la transformación affine
        image = src.read(1)  # Leer la primera banda de la imagen

    # Aplicar un umbral para detectar puntos en la imagen
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    # Convertir la imagen a booleano (si es necesario)
    threshold = 0 
    binary_image = (image > threshold).astype(np.uint8)

    # Extraer las formas (polígonos)
    shapes_gen = shapes(binary_image, mask=None, transform=transform)
    
    polygons = []
    for geom, _ in shapes_gen:
        polygons.append(shape(geom))

    # Asegurarse de que el directorio de salida existe
    output_dir = os.path.dirname(output_file)
    os.makedirs(output_dir, exist_ok=True)  # Crea el directorio si no existe

    # Encontrar los contornos de los puntos
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    escala = 250
    # Guardar las ubicaciones (coordenadas) y centroides en un archivo TXT
    with open(output_file, 'w') as f:
        for polygon in polygons:
            centroid = polygon.centroid  # Calcular el centroide
            f.write(f"Polígono:\n")
            for coord in coords:
                f.write(f"({coord[0]/escala}, {coord[1]/escala})\n")
            f.write(f"Centroide: ({centroid.x/escala}, {centroid.y/escala})\n")
            f.write("\n")  # Separar polígonos con una línea en blanco

# Ruta al archivo de entrada y salida
input_file = '/home/meli/planeargas/backend/src/imagen_raster/subidas_bajadas.tif'
output_file = '/home/meli/planeargas/backend/src/txt_resultantes/resultados_subidas_bajadas.txt'

# Procesar el archivo GeoTIFF para extraer puntos
process_geotiff_puntos(file_path, output_file, color)

# Llamar a la función
process_geotiff_subidas(input_file, output_file)
