import os
from _6_0_deteccion_rejillas import proceso_deteccion_rejilla

def test_proceso_deteccion_rejilla():
    input_image_path = '/home/meli/planeargas/backend/src/imagen_entrada/planta_1.png'
    output_directory = '/home/meli/planeargas/backend/src/detecciones/'
    
    # Asegurarse de que la carpeta de salida esté limpia antes de la prueba
    if os.path.exists(output_directory):
        for filename in os.listdir(output_directory):
            file_path = os.path.join(output_directory, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    
    # Ejecutar la función
    proceso_deteccion_rejilla(input_image_path)
    
    # Comprobar si el archivo de imagen fue creado
    expected_image_path = os.path.join(output_directory, 'plano_con_rejillas.png')
    assert os.path.isfile(expected_image_path), f"{expected_image_path} no fue creado."

    # Comprobar si el archivo de texto fue creado
    expected_txt_path = os.path.join(output_directory, 'ubicacion_rejillas.txt')
    assert os.path.isfile(expected_txt_path), f"{expected_txt_path} no fue creado."
    
    # Leer el contenido del archivo de texto
    with open(expected_txt_path, 'r') as file:
        contenido_txt = file.read()
    
    # Contenido esperado en el archivo txt
    contenido_esperado = """Rejilla 1: X = 1188, Y = 779
Rejilla 2: X = 1164, Y = 228"""
    
    # Verificar que el contenido del archivo txt sea el esperado
    assert contenido_txt.strip() == contenido_esperado, "El contenido del archivo txt no coincide con lo esperado."
