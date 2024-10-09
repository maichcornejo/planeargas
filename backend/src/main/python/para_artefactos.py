import os
from _1_0_procesamiento_imagen import procesar_imagen
from _2_0_png_to_geotiff import convertir_png_a_geotiff
from _3_0_0_extraer_caneria_copy import process_geotiff_caneria

# Rutas de entrada y salida
entrada_image_path = '/home/meli/planeargas/backend/src/imagen_entrada/isometrica/3.png'
salida_directory = '/home/meli/planeargas/backend/src/imagen_salida/'
rutas_imagenes = {
    'caneria': '/home/meli/planeargas/backend/src/imagen_salida/caneria.png',
    'artefactos': '/home/meli/planeargas/backend/src/imagen_salida/artefactos.png',
    'paredes': '/home/meli/planeargas/backend/src/imagen_salida/paredes.png',
    'subidas_bajadas': '/home/meli/planeargas/backend/src/imagen_salida/subidas_bajadas.png',
    'ventilaciones': '/home/meli/planeargas/backend/src/imagen_salida/ventilaciones.png',
    'cotas': '/home/meli/planeargas/backend/src/imagen_salida/cotas.png'
    }
output_directory = '/home/meli/planeargas/backend/src/imagen_raster/'
file_path_caneria = '/home/meli/planeargas/backend/src/imagen_raster/caneria.tif'
file_path_ventilaciones = '/home/meli/planeargas/backend/src/imagen_raster/ventilaciones.tif'
file_path_artefactos = '/home/meli/planeargas/backend/src/imagen_raster/artefactos.tif'
output_file_caneria = '/home/meli/planeargas/backend/src/txt_resultantes/resultados_caneria_iso.txt'
output_file_ventilaciones = '/home/meli/planeargas/backend/src/txt_resultantes/resultados_ventil_iso.txt'
output_file_artefactos = '/home/meli/planeargas/backend/src/txt_resultantes/resultados_artefac_iso.txt'
# Ejecutar el procesamiento
procesar_imagen(entrada_image_path, salida_directory)
convertir_png_a_geotiff(rutas_imagenes,output_directory)
process_geotiff_caneria(file_path_caneria, output_file_caneria, 'red')
process_geotiff_caneria(file_path_ventilaciones, output_file_ventilaciones, 'green')
process_geotiff_caneria(file_path_artefactos, output_file_artefactos, 'gray')