import cv2
import numpy as np

# Ruta para guardar el archivo TXT con la información de los ejes medianeros
OUTPUT_FILE_TXT = '/home/Maia/planeargas/backend/src/detecciones/ejes_medianeros.txt'

def detectar_ejes(ruta_imagen):
    # Cargar la imagen (paredes.png, para detectar ejes medianeros)
    imagen = cv2.imread(ruta_imagen)
    if imagen is None:
        print("Error al cargar la imagen de ejes.")
        return None, None

    # Convertir a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplicar desenfoque para reducir el ruido
    desenfocado = cv2.GaussianBlur(gris, (5, 5), 0)

    # Detectar bordes usando Canny
    bordes = cv2.Canny(desenfocado, 50, 150, apertureSize=3)

    # Detectar líneas usando la Transformada de Hough
    lines = cv2.HoughLinesP(bordes, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)

    if lines is None:
        print("No se detectaron líneas para los ejes medianeros.")
        return None, None

    # Filtrar líneas verticales (consideramos líneas con ángulo cercano a 90 grados)
    vertical_lines = []
    for line in lines:
        for x1, y1, x2, y2 in line:
            if abs(x2 - x1) < 10:  # Consideramos la línea como vertical si la diferencia en x es pequeña
                vertical_lines.append(line)

    if len(vertical_lines) < 2:
        print("No se detectaron suficientes líneas verticales para los ejes medianeros.")
        return None, None

    # Ordenar las líneas verticales por su posición x (para detectar la línea más a la izquierda y a la derecha)
    vertical_lines_sorted = sorted(vertical_lines, key=lambda line: (line[0][0] + line[0][2]) / 2)

    # Seleccionar las dos líneas más a la izquierda y a la derecha
    eje_izquierdo = vertical_lines_sorted[0][0]
    eje_derecho = vertical_lines_sorted[-1][0]

    # Obtener las posiciones x de los ejes medianeros
    x_eje_izquierdo = int((eje_izquierdo[0] + eje_izquierdo[2]) / 2)
    x_eje_derecho = int((eje_derecho[0] + eje_derecho[2]) / 2)

    print(f"Eje medianero izquierdo detectado en x={x_eje_izquierdo}")
    print(f"Eje medianero derecho detectado en x={x_eje_derecho}")

    return x_eje_izquierdo, x_eje_derecho

# Ruta de la imagen
ruta_imagen = '/home/Maia/planeargas/backend/src/imagen_salida/paredes.png'

# Detectar ejes medianeros
x_eje_izquierdo, x_eje_derecho = detectar_ejes(ruta_imagen)

# Si se detectaron los ejes correctamente, generar el archivo TXT
if x_eje_izquierdo is not None and x_eje_derecho is not None:
    with open(OUTPUT_FILE_TXT, "w") as archivo_txt:
        archivo_txt.write(f"Eje medianero izquierdo en x: {x_eje_izquierdo}\n")
        archivo_txt.write(f"Eje medianero derecho en x: {x_eje_derecho}\n")
    print(f"Archivo TXT '{OUTPUT_FILE_TXT}' generado con éxito.")
else:
    print("No se pudieron detectar los ejes medianeros correctamente.")
