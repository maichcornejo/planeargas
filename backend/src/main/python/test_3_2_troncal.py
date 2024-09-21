import os
import pytest
from _3_2_troncal import troncal_caneria



def test_troncal():

    ruta_entrada = "/home/meli/planeargas/backend/src/txt_resultantes/caneria_optimizada.txt"
    ruta_salida = "/home/meli/planeargas/backend/src/txt_resultantes/troncal_latex.txt"

    troncal_caneria(ruta_entrada, ruta_salida)

        # Contenido esperado del archivo generado
    contenido_esperado = """\\draw [color=red] (0, 0) -- (0, 0.2) -- (.5, .5) -- (.5, -2);
\\draw [color=red] (0.5, -2.0) -- (-1.2, -1.0);
\\draw [color=red] (-1.2, -1.0) -- (10.8, 5.9);
\\draw [color=red] (10.8, 5.9) -- (9.1, 6.9);
\\draw [color=red] (9.1, 6.9) -- (7.3, 5.9);
\\draw [color=red] (7.3, 5.9) -- (5.6, 6.9);
\\draw [color=red] (5.6, 6.9) -- (7.3, 5.9);
\\draw [color=red] (7.3, 5.9) -- (9.1, 6.9);"""

    # Leer el archivo generado
    with open(ruta_salida, 'r') as archivo_salida:
        contenido_generado = archivo_salida.read()

    # Verificar que el contenido generado sea igual al esperado
    assert contenido_generado.strip() == contenido_esperado.strip(), "El contenido del archivo generado no coincide con el esperado."
