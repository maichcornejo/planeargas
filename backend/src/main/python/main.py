import os
from _1_0_procesamiento_imagen import procesar_imagen
from _2_0_png_to_geotiff import convertir_png_a_geotiff
from _3_0_extraer_caneria import process_geotiff_caneria
from _3_1_normalizar_vectores import optimizar_caneria
from _3_2_troncal import troncal_caneria
from _4_0_extraer_subidas_bajadas import process_geotiff_subidas
from _5_0_1_detectar_medidor import proceso_principal_medidor
from _5_0_2_detectar_ejes_medidor import proceso_detectar_ejes_medianeros
from _5_1_distancia_medidor_ejes  import proceso_distancia_medidor
from _6_0_deteccion_rejillas import proceso_deteccion_rejilla
from _7_0_deteccion_llave_de_paso import proceso_deteccion_llave_de_paso


# Definir las rutas usadas en el código
rutas_imagenes = {
    'caneria': '/home/meli/planeargas/backend/src/imagen_salida/caneria.png',
    'artefactos': '/home/meli/planeargas/backend/src/imagen_salida/artefactos.png',
    'paredes': '/home/meli/planeargas/backend/src/imagen_salida/paredes.png',
    'subidas_bajadas': '/home/meli/planeargas/backend/src/imagen_salida/subidas_bajadas.png',
    'ventilaciones': '/home/meli/planeargas/backend/src/imagen_salida/ventilaciones.png',
    'cotas': '/home/meli/planeargas/backend/src/imagen_salida/cotas.png'
}

output_directory_raster = '/home/meli/planeargas/backend/src/imagen_raster/'
input_image_path = '/home/meli/planeargas/backend/src/imagen_entrada/planta_1.png'
output_directory_png = '/home/meli/planeargas/backend/src/imagen_salida/'
file_path_caneria_raster = '/home/meli/planeargas/backend/src/imagen_raster/caneria.tif'
file_path_resultados_caneria = '/home/meli/planeargas/backend/src/txt_resultantes/resultados_caneria_latex.txt'
path_caneria_optimizada = "/home/meli/planeargas/backend/src/txt_resultantes/caneria_optimizada.txt"
path_caneria_troncal = "/home/meli/planeargas/backend/src/txt_resultantes/troncal_latex.txt"
path_txt = '/home/meli/planeargas/backend/src/txt_resultantes/'
input_file_subidas = '/home/meli/planeargas/backend/src/imagen_raster/subidas_bajadas.tif'
output_file_subidas = '/home/meli/planeargas/backend/src/txt_resultantes/resultados_subidas_bajadas.txt'
tipo_caneria = "TUBO ACERO REVESTIDO POLIETILENO"
imagen_detectar_ejes_medianeros = '/home/meli/planeargas/backend/src/imagen_salida/paredes.png'


def main():
    procesar_imagen(input_image_path, output_directory_png)
    convertir_png_a_geotiff(rutas_imagenes, output_directory_raster)
    process_geotiff_caneria(file_path_caneria_raster, file_path_resultados_caneria)
    optimizar_caneria(file_path_resultados_caneria, path_caneria_optimizada)
    troncal_caneria(path_caneria_optimizada, path_caneria_troncal,tipo_caneria)
    process_geotiff_subidas(input_file_subidas, output_file_subidas)
    proceso_principal_medidor(input_image_path, 15.65)
    proceso_detectar_ejes_medianeros(imagen_detectar_ejes_medianeros)
    proceso_distancia_medidor(imagen_detectar_ejes_medianeros)
    proceso_deteccion_rejilla(input_image_path)
    proceso_deteccion_llave_de_paso(input_image_path)
main()


