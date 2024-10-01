import rasterio
from rasterio.transform import from_origin
from rasterio.crs import CRS
from PIL import Image
import numpy as np
import os

# Definir las rutas de las imágenes PNG y de salida GeoTIFF
rutas_imagenes = {
    'caneria': '/home/Maia/planeargas/backend/src/imagen_salida/caneria.png',
    'artefactos': '/home/Maia/planeargas/backend/src/imagen_salida/artefactos.png',
    'paredes': '/home/Maia/planeargas/backend/src/imagen_salida/paredes.png',
    'subidas_bajadas': '/home/Maia/planeargas/backend/src/imagen_salida/subidas_bajadas.png',
    'ventilaciones': '/home/Maia/planeargas/backend/src/imagen_salida/ventilaciones.png'
}

output_directory = '/home/Maia/planeargas/backend/src/imagen_raster/'

# Crear el directorio de salida si no existe
os.makedirs(output_directory, exist_ok=True)

# Definir la transformación geoespacial
transform = from_origin(west=0, north=0, xsize=1, ysize=1)

# Definir el sistema de referencia de coordenadas (CRS)
crs = CRS.from_epsg(4326)  # Cambia según la necesidad

# Crear un diccionario para mapear imágenes a sus índices de banda
banda_map = {
    'caneria': 0,         # Rojo
    'ventilaciones': 1    # Verde
}

for label, image_path in rutas_imagenes.items():
    # Cargar la imagen PNG
    png_image = Image.open(image_path)
    png_array = np.array(png_image)

    # Verificar si la imagen tiene un canal alfa (RGBA) o es RGB
    if png_array.shape[2] == 4:
        # Si es RGBA, convertirla a RGB eliminando el canal alfa
        png_array = png_array[:, :, :3]

    # Determinar el índice de banda para esta imagen
    band_index = banda_map.get(label, None)

    if band_index is not None and band_index < png_array.shape[2]:
        # Extraer la banda especificada
        single_band_array = png_array[:, :, band_index]
    else:
        # Si no se especifica el índice o es inválido, continuar con la imagen original
        single_band_array = png_array[:, :, 0]  # Por defecto toma la banda roja

    # Verificar y ajustar el rango de valores
    print(f"Imagen {label} - Max value: {np.max(single_band_array)}, Min value: {np.min(single_band_array)}")
    
    # Escalar los valores a 0-255 si es necesario
    if np.issubdtype(single_band_array.dtype, np.integer):
        single_band_array = single_band_array.astype(np.uint8)
    elif np.issubdtype(single_band_array.dtype, np.floating):
        single_band_array = (single_band_array * 255).astype(np.uint8)
    
    # Guardar la imagen como GeoTIFF de una sola banda
    output_path = os.path.join(output_directory, f'{label}.tif')
    with rasterio.open(
            output_path, 'w',
            driver='GTiff',
            height=single_band_array.shape[0],
            width=single_band_array.shape[1],
            count=1,  # Número de bandas
            dtype=single_band_array.dtype,
            crs=crs,
            transform=transform) as dst:

        # Guardar la única banda
        dst.write(single_band_array, 1)

    print(f"Imagen {label} guardada en {output_path}")
