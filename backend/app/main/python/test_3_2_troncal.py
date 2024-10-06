import os
import pytest
from _3_2_troncal import troncal_caneria



def test_troncal():

    ruta_entrada = "/home/meli/planeargas/backend/src/txt_resultantes/caneria_optimizada.txt"
    ruta_salida = "/home/meli/planeargas/backend/src/txt_resultantes/troncal_latex.txt"
    tipo_caneria = "TUBO ACERO REVESTIDO POLIETILENO"

    troncal_caneria(ruta_entrada, ruta_salida, tipo_caneria)

        # Contenido esperado del archivo generado
    contenido_esperado = """\\draw [color=red] (0, 0) -- (0, 0.2) -- (.5, .5) -- (.5, -2);\\node [rotate = 30] at (0.2, 0.5) {0.15};\\node [rotate = 90] at (0.3, -1.0) {0.90};
\\node [rotate = 30] at (8.6, 2.9) {23.45};
\\draw [color=red] (0.5, -2.0) -- (16.7, 7.4);
\\node [rotate = 30] at (8.6, 2.4) {TUBO ACERO REVESTIDO POLIETILENO};
\\node [rotate = -30] at (18.9, 6.4) {6.27};
\\draw [color=red] (16.7, 7.4) -- (21.1, 4.9);
\\node [rotate = -30] at (18.9, 5.9) {T.A.R.P.};
\\node [rotate = 30] at (24.7, 7.2) {10.32};
\\draw [color=red] (21.1, 4.9) -- (28.2, 9.0);
\\node [rotate = 30] at (24.7, 6.7) {TUBO ACERO REVESTIDO POLIETILENO};
\\node [rotate = -30] at (27.7, 9.5) {0.22};
\\draw [color=red] (28.2, 9.0) -- (27.2, 9.6);

\\node [rotate = -30] at (27.7, 9.5) {0.22};
\\draw [color=red] (28.2, 9.0) -- (27.2, 9.6);

"""

    # Leer el archivo generado
    with open(ruta_salida, 'r') as archivo_salida:
        contenido_generado = archivo_salida.read()

    # Verificar que el contenido generado sea igual al esperado
    assert contenido_generado.strip() == contenido_esperado.strip(), "El contenido del archivo generado no coincide con el esperado."
