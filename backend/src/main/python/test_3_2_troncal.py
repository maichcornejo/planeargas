import os
import pytest
from _3_2_troncal import troncal_caneria



def test_troncal():

    ruta_entrada = "/home/meli/planeargas/backend/src/txt_resultantes/caneria_optimizada.txt"
    ruta_salida = "/home/meli/planeargas/backend/src/txt_resultantes/troncal_latex.txt"

    troncal_caneria(ruta_entrada, ruta_salida)

        # Contenido esperado del archivo generado
    contenido_esperado = """\\draw [color=red] (0, 0) -- (0, 0.2) -- (.5, .5) -- (.5, -2);
\\draw [color=red] (0.5, -2.0) -- (16.7, 7.4);
\\draw [color=red] (16.7, 7.4) -- (21.1, 4.9);
\\draw [color=red] (21.1, 4.9) -- (28.2, 9.0);
\\draw [color=red] (28.2, 9.0) -- (26.5, 10.0);
\\draw [color=red] (26.5, 10.0) -- (28.2, 9.0);"""

    # Leer el archivo generado
    with open(ruta_salida, 'r') as archivo_salida:
        contenido_generado = archivo_salida.read()

    # Verificar que el contenido generado sea igual al esperado
    assert contenido_generado.strip() == contenido_esperado.strip(), "El contenido del archivo generado no coincide con el esperado."
