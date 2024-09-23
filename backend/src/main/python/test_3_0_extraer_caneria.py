import os
import pytest
from _3_0_extraer_caneria import process_geotiff_caneria

# Ruta al archivo de entrada y salida
input_file_path = '/home/meli/planeargas/backend/src/imagen_raster/caneria.tif'
output_file_path = '/home/meli/planeargas/backend/src/txt_resultantes/resultados_caneria_latex.txt'

# Ejecutar la función principal para extraer cañería
process_geotiff_caneria(input_file_path, output_file_path)

def test_process_geotiff_caneria():

    # Definir el contenido esperado en el archivo de salida
    contenido_esperado = """\\draw [color=red] (1.79, 14.26) -- (1.79, 4.88);
\\draw [color=red] (4.30, 4.88) -- (4.30, 0.75);
\\draw [color=red] (1.79, 4.88) -- (4.30, 4.88);
\\draw [color=red] (1.90, 3.18) -- (4.30, 3.18);
\\draw [color=red] (4.30, 1.57) -- (4.90, 1.57);
\\draw [color=red] (1.90, 3.18) -- (1.90, 3.03);
\\draw [color=red] (1.81, 3.09) -- (1.91, 3.09);
\\draw [color=red] (1.70, 14.36) -- (1.70, 14.26);
\\draw [color=red] (4.89, 1.52) -- (5.04, 1.52);
\\draw [color=red] (4.21, 0.76) -- (4.30, 0.76);
\\draw [color=red] (4.28, 0.82) -- (4.33, 0.82);
\\draw [color=red] (4.87, 1.59) -- (4.94, 1.59);
\\draw [color=red] (1.87, 3.03) -- (1.94, 3.03);
\\draw [color=red] (4.90, 1.58) -- (4.90, 1.52);
"""


    # Verificar que el archivo de salida se haya creado
    assert os.path.exists(output_file_path), "El archivo de salida no fue creado."

    # Leer el contenido generado del archivo de salida
    with open(output_file_path, 'r') as f:
        contenido_generado = f.read()

    # Comparar el contenido generado con el contenido esperado
    assert contenido_generado.strip() == contenido_esperado.strip(), "El contenido del archivo de salida no es correcto."