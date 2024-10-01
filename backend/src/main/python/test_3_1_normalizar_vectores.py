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
    contenido_esperado = """\\draw [color=red] (1.7, 14.36) -- (1.7, 14.26);
\\draw [color=red] (1.79, 14.26) -- (1.79, 4.88);
\\draw [color=red] (1.79, 4.88) -- (4.3, 4.88);
\\draw [color=red] (4.3, 4.88) -- (4.3, 0.75);
\\draw [color=red] (4.21, 0.76) -- (4.3, 0.76);
\\draw [color=red] (4.28, 0.82) -- (4.33, 0.82);"""


    # Leer el archivo generado
    with open(ruta_salida, 'r') as archivo_salida:
        contenido_generado = archivo_salida.read()

    # Verificar que el contenido generado sea igual al esperado
    assert contenido_generado.strip() == contenido_esperado.strip(), "El contenido del archivo generado no coincide con el esperado."

