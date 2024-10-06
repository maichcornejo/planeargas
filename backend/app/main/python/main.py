import os
import cv2
from _1_0_procesamiento_imagen import procesar_imagen
from _2_0_png_to_geotiff import convertir_png_a_geotiff
from _3_0_extraer_caneria import process_geotiff_caneria
from _3_1_normalizar_vectores import optimizar_caneria
from _3_2_troncal import troncal_caneria
from _4_0_extraer_subidas_bajadas import process_geotiff_puntos
from _5_0_1_detectar_medidor import proceso_principal_medidor
from _5_0_2_detectar_ejes_medidor import proceso_detectar_ejes_medianeros
from _5_1_distancia_medidor_ejes import proceso_distancia_medidor
from _6_0_deteccion_rejillas import proceso_deteccion_rejilla
from _7_0_deteccion_llave_de_paso import proceso_deteccion_llave_de_paso
from _9_0_identificacion_artefactos import identificar_artefactos

# Definir las rutas usadas en el código
rutas_imagenes = {
    'caneria': '/home/Maia/planeargas/backend/app/imagen_salida/caneria.png',
    'artefactos': '/home/Maia/planeargas/backend/app/imagen_salida/artefactos.png',
    'paredes': '/home/Maia/planeargas/backend/app/imagen_salida/paredes.png',
    'subidas_bajadas': '/home/Maia/planeargas/backend/app/imagen_salida/subidas_bajadas.png',
    'ventilaciones': '/home/Maia/planeargas/backend/app/imagen_salida/ventilaciones.png',
    'cotas': '/home/Maia/planeargas/backend/app/imagen_salida/cotas.png'
}

output_directory_raster = '/home/Maia/planeargas/backend/app/imagen_raster/'
input_image_path = '/home/Maia/planeargas/backend/app/imagen_entrada/planta_4.png'
output_directory_png = '/home/Maia/planeargas/backend/app/imagen_salida/'
file_path_caneria_raster = '/home/Maia/planeargas/backend/app/imagen_raster/caneria.tif'
file_path_resultados_caneria = '/home/Maia/planeargas/backend/app/txt_resultantes/resultados_caneria_latex.txt'
path_caneria_optimizada = "/home/Maia/planeargas/backend/app/txt_resultantes/caneria_optimizada.txt"
path_caneria_troncal = "/home/Maia/planeargas/backend/app/txt_resultantes/troncal_latex.txt"
path_txt = '/home/Maia/planeargas/backend/app/txt_resultantes/'
input_file_subidas = '/home/Maia/planeargas/backend/app/imagen_raster/subidas_bajadas.tif'
output_file_subidas = '/home/Maia/planeargas/backend/app/txt_resultantes/resultados_subidas_bajadas.txt'
tipo_caneria = "TUBO ACERO REVESTIDO POLIETILENO"
imagen_detectar_ejes_medianeros = '/home/Maia/planeargas/backend/app/imagen_salida/paredes.png'

# Paràmetros de la base de datos (modifica según tu configuración)
db_params = {
    'dbname': 'tu_db',
    'user': 'tu_usuario',
    'host': 'localhost',
    'password': 'tu_password'
}

def main():
    # Procesos previos de la imagen
    procesar_imagen(input_image_path, output_directory_png)
    convertir_png_a_geotiff(rutas_imagenes, output_directory_raster)
    process_geotiff_caneria(file_path_caneria_raster, file_path_resultados_caneria, 'red')
    optimizar_caneria(file_path_resultados_caneria, path_caneria_optimizada)
    troncal_caneria(path_caneria_optimizada, path_caneria_troncal, tipo_caneria)
    process_geotiff_puntos(input_file_subidas, output_file_subidas, 'blue')
    proceso_principal_medidor(input_image_path, 12.5)
    proceso_detectar_ejes_medianeros(imagen_detectar_ejes_medianeros)
    proceso_distancia_medidor(imagen_detectar_ejes_medianeros)
    proceso_deteccion_rejilla(input_image_path)
    proceso_deteccion_llave_de_paso(input_image_path)

    # Detección de artefactos
    img_plano = cv2.imread(input_image_path)  # Cargar la imagen del plano
    detector = identificar_artefactos(db_params)  # Inicializar la clase con los parámetros de la base de datos
    detector.procesar_artefactos(img_plano)  # Llamar al método para procesar la detección de artefactos

# Ejecutar la función principal
if __name__ == "__main__":
    main()
