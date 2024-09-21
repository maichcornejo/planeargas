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
    contenido_esperado = """\\draw [color=red] (5.45, 14.19) -- (5.45, 7.25);
\\draw [color=red] (4.58, 7.25) -- (5.44, 7.25);
\\draw [color=red] (4.41, 7.39) -- (4.58, 7.39);
\\draw [color=red] (5.48, 14.55) -- (5.48, 14.36);
\\draw [color=red] (5.08, 7.47) -- (5.19, 7.47);
\\draw [color=red] (4.49, 7.47) -- (4.60, 7.47);
\\draw [color=red] (5.17, 7.39) -- (5.31, 7.39);
\\draw [color=red] (5.62, 14.36) -- (5.62, 14.21);
\\draw [color=red] (5.45, 14.19) -- (5.60, 14.19);
\\draw [color=red] (5.11, 7.39) -- (5.11, 7.30);
\\draw [color=red] (4.58, 7.38) -- (4.58, 7.30);
\\draw [color=red] (5.14, 7.46) -- (5.14, 7.39);
\\draw [color=red] (4.54, 7.46) -- (4.54, 7.39);
"""


    # Verificar que el archivo de salida se haya creado
    assert os.path.exists(output_file_path), "El archivo de salida no fue creado."

    # Leer el contenido generado del archivo de salida
    with open(output_file_path, 'r') as f:
        contenido_generado = f.read()

    # Comparar el contenido generado con el contenido esperado
    assert contenido_generado.strip() == contenido_esperado.strip(), "El contenido del archivo de salida no es correcto."