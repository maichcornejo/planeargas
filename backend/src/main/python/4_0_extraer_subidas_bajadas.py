import os
import rasterio
import numpy as np
from rasterio.features import shapes
from shapely.geometry import shape

def process_geotiff(file_path, output_file):
    # Cargar el archivo GeoTIFF
    with rasterio.open(file_path) as src:
        # Leer la imagen y la transformación affine
        image = src.read(1)  # Leer la primera banda de la imagen
        transform = src.transform

    # Convertir la imagen a booleano (si es necesario)
    threshold = 0  # Cambia esto si necesitas un umbral diferente
    binary_image = (image > threshold).astype(np.uint8)

    # Extraer las formas (polígonos)
    shapes_gen = shapes(binary_image, mask=None, transform=transform)
    
    polygons = []
    for geom, _ in shapes_gen:
        polygons.append(shape(geom))

    # Asegurarse de que el directorio de salida existe
    output_dir = os.path.dirname(output_file)
    os.makedirs(output_dir, exist_ok=True)  # Crea el directorio si no existe

    # Guardar las ubicaciones (coordenadas) y centroides en un archivo TXT
    with open(output_file, 'w') as f:
        for polygon in polygons:
            coords = list(polygon.exterior.coords)
            centroid = polygon.centroid  # Calcular el centroide
            f.write(f"Polígono:\n")
            for coord in coords:
                f.write(f"({coord[0]}, {coord[1]})\n")
            f.write(f"Centroide: ({centroid.x}, {centroid.y})\n")
            f.write("\n")  # Separar polígonos con una línea en blanco

# Ruta al archivo de entrada y salida
input_file = '/home/meli/planeargas/backend/src/imagen_raster/subidas_bajadas.tif'
output_file = '/home/meli/planeargas/backend/src/txt_resultantes/resultados_subidas_bajadas.txt'

# Llamar a la función
process_geotiff(input_file, output_file)

