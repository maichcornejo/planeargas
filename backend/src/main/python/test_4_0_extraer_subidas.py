import os
import pytest
from _4_0_extraer_subidas_bajadas import process_geotiff_puntos

def test_process_geotiff_puntos():

    input_file_subidas = '/home/meli/planeargas/backend/src/imagen_raster/subidas_bajadas.tif'
    color = 'blue'
    output_file_subidas = '/home/meli/planeargas/backend/src/txt_resultantes/resultados_subidas_bajadas.txt'

    process_geotiff_puntos(input_file_subidas, output_file_subidas, color)

            # Contenido esperado del archivo generado
<<<<<<< HEAD
    contenido_esperado = """\\fill [color=blue] (1.79, 14.21) circle (1pt);
\\fill [color=blue] (1.91, 3.10) circle (1pt);
\\fill [color=blue] (4.90, 1.53) circle (1pt);
\\fill [color=blue] (4.30, 0.76) circle (1pt);
=======
    contenido_esperado = """(4.298, -0.754)
(1.914, -3.09)
(1.798, -14.198)
(4.320009526743253, -7.680019730334017)
>>>>>>> aa5cfefab (cambie las imagenes de entrada)
"""

    # Leer el archivo generado
    with open(output_file_subidas, 'r') as archivo_salida:
        contenido_generado = archivo_salida.read()

    # Verificar que el contenido generado sea igual al esperado
    assert contenido_generado.strip() == contenido_esperado.strip(), "El contenido del archivo generado no coincide con el esperado."
