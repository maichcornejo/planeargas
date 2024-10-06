import os
import rasterio
import numpy as np
from PIL import Image
from _2_0_png_to_geotiff import convertir_png_a_geotiff

# Definir las rutas usadas en el código principal
rutas_imagenes = {
    'caneria': '/home/meli/planeargas/backend/src/imagen_salida/caneria.png',
    'artefactos': '/home/meli/planeargas/backend/src/imagen_salida/artefactos.png',
    'paredes': '/home/meli/planeargas/backend/src/imagen_salida/paredes.png',
    'subidas_bajadas': '/home/meli/planeargas/backend/src/imagen_salida/subidas_bajadas.png',
    'ventilaciones': '/home/meli/planeargas/backend/src/imagen_salida/ventilaciones.png'
}

output_directory = '/home/meli/planeargas/backend/src/imagen_raster/'

def test_output_images_exist():
    for label in rutas_imagenes.keys():
        output_image_path = os.path.join(output_directory, f'{label}.tif')
        assert os.path.exists(output_image_path), f"El archivo {label}.tif no se guardó correctamente."

def test_image_dimensions_and_dtype():
    for label, image_path in rutas_imagenes.items():
        png_image = Image.open(image_path)
        png_array = np.array(png_image)

        output_image_path = os.path.join(output_directory, f'{label}.tif')
        with rasterio.open(output_image_path) as src:
            assert src.width == png_array.shape[1], f"El ancho de la imagen {label} no coincide."
            assert src.height == png_array.shape[0], f"El alto de la imagen {label} no coincide."
            assert src.dtypes[0] == 'uint8', f"El tipo de datos de {label}.tif no es uint8."

def test_geospatial_metadata():
    for label in rutas_imagenes.keys():
        output_image_path = os.path.join(output_directory, f'{label}.tif')
        with rasterio.open(output_image_path) as src:
            assert src.crs.to_string() == 'EPSG:4326', f"El CRS de {label}.tif no es EPSG:4326."
            assert src.transform == rasterio.transform.from_origin(0, 0, 1, 1), f"La transformación geoespacial de {label}.tif no es correcta."

# Ejecutar la función principal para convertir imágenes
convertir_png_a_geotiff(rutas_imagenes, output_directory)
