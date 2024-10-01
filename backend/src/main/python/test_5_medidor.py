import os
from _5_1_distancia_medidor_ejes import proceso_distancia_medidor

def test_proceso_distancia_medidor():
    input_image_path = '/home/meli/planeargas/backend/src/imagen_salida/paredes.png'
    output_directory = '/home/meli/planeargas/backend/src/detecciones/'
    
    # Asegurarse de que la carpeta de salida esté limpia antes de la prueba
    if os.path.exists(output_directory):
        for filename in os.listdir(output_directory):
            file_path = os.path.join(output_directory, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    
    # Ejecutar la función
    proceso_distancia_medidor(input_image_path)
    
    # Comprobar si el archivo txt fue creado y tiene el contenido esperado
    expected_txt_path = os.path.join(output_directory, 'distancia_medidor_ejes.txt')
    assert os.path.isfile(expected_txt_path), f"{expected_txt_path} no fue creado."
    
    with open(expected_txt_path, 'r') as file:
        contenido_txt = file.read()
    
    # Contenido esperado en el archivo txt
    contenido_esperado = """Eje Medianero Izquierdo (X): 399 píxeles
Eje Medianero Derecho (X): 1733 píxeles
Longitud del Eje Municipal en Píxeles: 1334 píxeles
Longitud del Eje Municipal en Metros: 15.65 m
Distancia desde el Medidor al Eje Izquierdo: 0.45 m
Distancia desde el Medidor al Eje Derecho: 15.20 m"""
    
    assert contenido_txt.strip() == contenido_esperado, "El contenido del archivo txt no coincide con lo esperado."
    
    # Comprobar si el archivo PNG fue creado
    expected_png_path = os.path.join(output_directory, 'distancia_medidor_visual.png')
    assert os.path.isfile(expected_png_path), f"{expected_png_path} no fue creado."
