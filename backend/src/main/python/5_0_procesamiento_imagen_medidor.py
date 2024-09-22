import cv2
import numpy as np

def detectar_perimetro_y_medidor(ruta_imagen, escala_pixeles_metro=100):
    # Cargar la imagen
    imagen = cv2.imread(ruta_imagen)
    if imagen is None:
        print("Error al cargar la imagen.")
        return

    # Convertir a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplicar desenfoque para reducir el ruido
    desenfocado = cv2.GaussianBlur(gris, (5, 5), 0)

    # Aplicar umbral adaptativo para mejorar la detección de bordes
    umbral = cv2.adaptiveThreshold(desenfocado, 255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2)

    # Aplicar operaciones morfológicas para cerrar brechas en los bordes
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    cerrado = cv2.morphologyEx(umbral, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Detectar bordes usando Canny
    bordes = cv2.Canny(cerrado, 50, 150, apertureSize=3)

    # Opcional: Mostrar etapas intermedias para depuración
    # cv2.imshow("Gris", gris)
    # cv2.imshow("Desenfocado", desenfocado)
    # cv2.imshow("Umbral Adaptativo", umbral)
    # cv2.imshow("Cerrado Morfológico", cerrado)
    # cv2.imshow("Bordes Canny", bordes)
    # cv2.waitKey(0)

    # Encontrar contornos
    contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Inicializar variables para almacenar los rectángulos detectados
    rect_perimetro = None
    rect_medidor = None

    # Definir las dimensiones reales del medidor en metros
    ancho_medidor_real = 0.40  # metros
    alto_medidor_real = 0.30   # metros

    # Iterar sobre cada contorno detectado
    for contorno in contornos:
        # Aproximar el contorno a un polígono
        peri = cv2.arcLength(contorno, True)
        approx = cv2.approxPolyDP(contorno, 0.02 * peri, True)

        # Si el polígono tiene 4 vértices, es un rectángulo
        if len(approx) == 4:
            # Obtener el bounding rect
            x, y, w, h = cv2.boundingRect(approx)

            # Calcular dimensiones reales
            ancho_real = w / escala_pixeles_metro
            alto_real = h / escala_pixeles_metro

            # Definir un margen de tolerancia para las dimensiones del medidor
            margen = 0.05  # 5 cm de margen

            # Verificar si coincide con las dimensiones del medidor
            if (abs(ancho_real - ancho_medidor_real) <= margen) and (abs(alto_real - alto_medidor_real) <= margen):
                rect_medidor = (x, y, w, h)
                cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(imagen, "Medidor de Gas", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            else:
                # Asumimos que el perímetro de la propiedad es el rectángulo más grande
                area = w * h
                if rect_perimetro is None or area > (rect_perimetro[2] * rect_perimetro[3]):
                    rect_perimetro = (x, y, w, h)

    # Dibujar el perímetro de la propiedad
    if rect_perimetro:
        x, y, w, h = rect_perimetro
        cv2.rectangle(imagen, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(imagen, "Perimetro Propiedad", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Extraer solo el perímetro de la propiedad
        perimetro_extraido = imagen[y:y+h, x:x+w]
        cv2.imshow("Perimetro Extraido", perimetro_extraido)
        cv2.imwrite("perimetro_extraido.png", perimetro_extraido)
    else:
        print("No se detectó el perímetro de la propiedad.")

    # Mostrar la imagen resultante con las anotaciones
    cv2.imshow("Deteccion", imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Opcional: retornar las coordenadas
    return rect_perimetro, rect_medidor

# Ejemplo de uso
ruta = '/home/Maia/planeargas/backend/src/imagen_entrada/planta_1.png'  # Archivo PNG subido
perimetro, medidor = detectar_perimetro_y_medidor(ruta)
if perimetro:
    print(f"Perímetro de la propiedad: x={perimetro[0]}, y={perimetro[1]}, ancho={perimetro[2]}, alto={perimetro[3]}")
if medidor:
    print(f"Medidor de gas: x={medidor[0]}, y={medidor[1]}, ancho={medidor[2]}, alto={medidor[3]}")
