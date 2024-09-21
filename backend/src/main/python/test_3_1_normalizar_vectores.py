import os
import pytest
from _3_1_normalizar_vectores import optimizar_caneria



def test_optimizar_caneria():
    # Ruta de los archivos de entrada para la prueba
    ruta_entrada = "/home/meli/planeargas/backend/src/txt_resultantes/resultados_caneria_latex.txt"
    ruta_salida = "/home/meli/planeargas/backend/src/txt_resultantes/caneria_optimizada.txt"

    # Ejecutar la función principal
    try:
        optimizar_caneria(ruta_entrada, ruta_salida)
    except Exception as e:
        pytest.fail(f"Ocurrió un error durante el procesamiento: {e}")

    # Contenido esperado del archivo generado
    contenido_esperado = """\\draw [color=red] (5.48, 14.55) -- (5.48, 14.36);
\\draw [color=red] (5.62, 14.36) -- (5.62, 14.21);
\\draw [color=red] (5.45, 14.19) -- (5.6, 14.19);
\\draw [color=red] (5.45, 14.19) -- (5.45, 7.25);
\\draw [color=red] (4.58, 7.25) -- (5.44, 7.25);
\\draw [color=red] (4.58, 7.38) -- (4.58, 7.3);
\\draw [color=red] (4.41, 7.39) -- (4.58, 7.39);
\\draw [color=red] (4.49, 7.47) -- (4.6, 7.47);
\\draw [color=red] (4.54, 7.46) -- (4.54, 7.39);"""


    # Leer el archivo generado
    with open(ruta_salida, 'r') as archivo_salida:
        contenido_generado = archivo_salida.read()

    # Verificar que el contenido generado sea igual al esperado
    assert contenido_generado.strip() == contenido_esperado.strip(), "El contenido del archivo generado no coincide con el esperado."

