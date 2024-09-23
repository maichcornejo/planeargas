import os
import pytest
from _4_0_extraer_subidas_bajadas import process_geotiff_subidas

def test_extraer_subidas():

    input_file_subidas = '/home/meli/planeargas/backend/src/imagen_raster/subidas_bajadas.tif'
    output_file_subidas = '/home/meli/planeargas/backend/src/txt_resultantes/resultados_subidas_bajadas.txt'

    process_geotiff_subidas(input_file_subidas, output_file_subidas)

            # Contenido esperado del archivo generado
    contenido_esperado = """(4.298, -0.754)
(4.91, -1.522)
(1.914, -3.09)
(1.798, -14.198)
(4.320009526743253, -7.680019730334017)
"""

    # Leer el archivo generado
    with open(output_file_subidas, 'r') as archivo_salida:
        contenido_generado = archivo_salida.read()

    # Verificar que el contenido generado sea igual al esperado
    assert contenido_generado.strip() == contenido_esperado.strip(), "El contenido del archivo generado no coincide con el esperado."
