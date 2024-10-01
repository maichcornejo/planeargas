import os
from _7_0_deteccion_llave_de_paso import proceso_deteccion_llave_de_paso  # Asegúrate de importar correctamente tu función

def test_proceso_deteccion_llave_de_paso():
    input_image_path = '/home/meli/planeargas/backend/src/imagen_entrada/planta_1.png'
    output_directory = '/home/meli/planeargas/backend/src/detecciones/'
    
    # Asegurarse de que la carpeta de salida esté limpia antes de la prueba
    if os.path.exists(output_directory):
        for filename in os.listdir(output_directory):
            file_path = os.path.join(output_directory, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    
    # Ejecutar la función
    proceso_deteccion_llave_de_paso(input_image_path)
    
    # Comprobar si el archivo de imagen fue creado
    expected_image_path = os.path.join(output_directory, 'artefactos_y_llaves_exactos.png')
    assert os.path.isfile(expected_image_path), f"{expected_image_path} no fue creado."

    # Comprobar si el archivo de texto fue creado
    expected_txt_path = os.path.join(output_directory, 'deteccion_llaves_exactas.txt')
    assert os.path.isfile(expected_txt_path), f"{expected_txt_path} no fue creado."
    
    # Leer el contenido del archivo de texto
    with open(expected_txt_path, 'r') as file:
        contenido_txt = file.read()
    
    # Contenido esperado en el archivo txt
    contenido_esperado = """Artefacto 1 en (441, 760) tiene la llave a la izquierda.
Artefacto 2 en (1275, 391) tiene la llave a la derecha.
Artefacto 3 en (1040, 220) tiene la llave a la izquierda."""
    
    # Verificar que el contenido del archivo txt sea el esperado
    assert contenido_txt.strip() == contenido_esperado, "El contenido del archivo txt no coincide con lo esperado."
