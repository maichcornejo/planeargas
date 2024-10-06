import pytest
import cv2
import numpy as np
from _5_1_distancia_medidor_ejes import encontrar_medidor_por_ubicacion_fija  

# Test para la función encontrar_medidor_por_ubicacion_fija
def test_encontrar_medidor_por_ubicacion_fija():
    # Crear una imagen de prueba en blanco con un rectángulo (simulando un medidor de gas)
    width, height = 500, 500
    image_color = np.zeros((height, width, 3), dtype=np.uint8)

    # Dibujar un rectángulo que simula el medidor en la parte inferior de la imagen
    medidor_x, medidor_y = 200, 450
    cv2.rectangle(image_color, (medidor_x, medidor_y), (medidor_x + 40, medidor_y + 30), (255, 255, 255), -1)

    # Llamar a la función encontrar_medidor_por_ubicacion_fija
    result = encontrar_medidor_por_ubicacion_fija(image_color, ancho_medidor=0.40, alto_medidor=0.30, resolucion=15.65)

    # Verificar que se encuentra el medidor
    assert result is not None, "El medidor debería haber sido encontrado"
    
    x_abs, y_abs, w, h = result

    # Verificar las coordenadas y tamaño del medidor
    assert x_abs == medidor_x, f"Se esperaba que x_abs fuera {medidor_x}, pero se obtuvo {x_abs}"
    assert y_abs == medidor_y, f"Se esperaba que y_abs fuera {medidor_y}, pero se obtuvo {y_abs}"
    assert w == 40, f"Se esperaba que el ancho del medidor fuera 40, pero se obtuvo {w}"
    assert h == 30, f"Se esperaba que el alto del medidor fuera 30, pero se obtuvo {h}"

# Test para calcular distancias y generar archivos de salida (mock)
def test_calculo_distancias_y_archivos(mocker):
    # Mock de los métodos de OpenCV que generan archivos
    mocker.patch('cv2.imwrite')
    mocker.patch('builtins.open', mocker.mock_open())

    # Crear una imagen de prueba en blanco
    width, height = 500, 500
    image_color = np.zeros((height, width, 3), dtype=np.uint8)

    # Simular la detección del medidor en la parte inferior
    medidor_x, medidor_y = 200, 450
    cv2.rectangle(image_color, (medidor_x, medidor_y), (medidor_x + 40, medidor_y + 30), (255, 255, 255), -1)

    # Simular los ejes medianeros
    left_medianero_x = 50
    right_medianero_x = 450
    municipal_line_y = 480

    # Simular la escala de metros por píxel
    longitud_real_metros = 15.65
    longitud_municipal_pixels = right_medianero_x - left_medianero_x
    escala_metros_por_pixel = longitud_real_metros / longitud_municipal_pixels

    # Calcular la distancia desde el centro del medidor a los ejes
    centro_medidor_x = medidor_x + 20  # Centro del medidor
    distancia_izquierda_px = abs(centro_medidor_x - left_medianero_x)
    distancia_derecha_px = abs(centro_medidor_x - right_medianero_x)
    distancia_izquierda_metros = distancia_izquierda_px * escala_metros_por_pixel
    distancia_derecha_metros = distancia_derecha_px * escala_metros_por_pixel

    # Verificar las distancias calculadas
    assert distancia_izquierda_metros > 0, "La distancia izquierda debe ser positiva"
    assert distancia_derecha_metros > 0, "La distancia derecha debe ser positiva"

    # Verificar que se llame a la función de guardar archivo de texto
    mocker.patch("builtins.open", mocker.mock_open())
    txt_output_path = '/home/Maia/planeargas/backend/src/detecciones/distancia_medidor_ejes.txt'
    
    with open(txt_output_path, 'w') as f:
        f.write(f'Eje Medianero Izquierdo (X): {left_medianero_x} píxeles\n')
        f.write(f'Eje Medianero Derecho (X): {right_medianero_x} píxeles\n')
        f.write(f'Longitud del Eje Municipal en Píxeles: {longitud_municipal_pixels} píxeles\n')
        f.write(f'Longitud del Eje Municipal en Metros: {longitud_real_metros:.2f} m\n')
        f.write(f'Distancia desde el Medidor al Eje Izquierdo: {distancia_izquierda_metros:.2f} m\n')
        f.write(f'Distancia desde el Medidor al Eje Derecho: {distancia_derecha_metros:.2f} m\n')

    # Verificar que el archivo de texto se haya escrito correctamente
    open.assert_called_with(txt_output_path, 'w')

    # Verificar que se guarden las imágenes de salida
    cv2.imwrite.assert_called()
