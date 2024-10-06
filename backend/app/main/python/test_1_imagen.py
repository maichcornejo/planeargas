# test_procesamiento_imagen.py

import os
from _1_0_procesamiento_imagen import procesar_imagen

def test_procesar_imagen():
    input_image_path = '/home/meli/planeargas/backend/src/imagen_entrada/planta_1.png'
    output_directory = '/home/meli/planeargas/backend/src/imagen_salida/'
    
    # Asegurarse de que la carpeta de salida esté limpia antes de la prueba
    if os.path.exists(output_directory):
        for filename in os.listdir(output_directory):
            file_path = os.path.join(output_directory, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    
    # Ejecutar la función
    procesar_imagen(input_image_path, output_directory)

    # Comprobar si se generaron las imágenes esperadas
    expected_files = ['caneria.png', 'subidas_bajadas.png', 'ventilaciones.png', 'paredes.png', 'artefactos.png']
    for expected_file in expected_files:
        assert os.path.isfile(os.path.join(output_directory, expected_file)), f"{expected_file} no fue creado."
