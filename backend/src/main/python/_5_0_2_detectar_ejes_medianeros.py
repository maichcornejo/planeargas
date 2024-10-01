import cv2
import numpy as np

# Cargar la imagen
image_path = '/home/Maia/planeargas/backend/src/imagen_salida/paredes.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Aplicar un umbral para detectar las líneas
_, thresh = cv2.threshold(image, 240, 255, cv2.THRESH_BINARY_INV)

# Detectar bordes
edges = cv2.Canny(thresh, 50, 150, apertureSize=3)

# Detectar líneas usando la Transformada de Hough
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 150, minLineLength=120, maxLineGap=10)

# Inicializar variables para almacenar las coordenadas de los ejes medianeros
left_medianero_x = float('inf')  # La coordenada x más pequeña
right_medianero_x = -float('inf')  # La coordenada x más grande
municipal_line_y = None

# Verificar si se han detectado líneas
if lines is not None:
    # Dibujar todas las líneas detectadas para depuración
    output_image_debug = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(output_image_debug, (x1, y1), (x2, y2), (255, 0, 0), 2)

    cv2.imwrite('/home/Maia/planeargas/backend/src/detecciones/lineas_detectadas_debug.png', output_image_debug)

    # Iterar sobre las líneas detectadas
    for line in lines:
        x1, y1, x2, y2 = line[0]
        
        # Si la línea es vertical (misma coordenada x con margen de error)
        if abs(x1 - x2) < 10:  # Estricta condición para detectar líneas casi verticales
            # Actualizar la coordenada del eje medianero izquierdo (la x más pequeña)
            if x1 < left_medianero_x:
                left_medianero_x = x1
            
            # Actualizar la coordenada del eje medianero derecho (la x más grande)
            if x1 > right_medianero_x:
                right_medianero_x = x1
        
        # Detectar la línea municipal, que es la línea horizontal más baja
        if abs(y1 - y2) < 10:
            if municipal_line_y is None or y1 > municipal_line_y:
                municipal_line_y = y1

# Imprimir los resultados
print(f'Eje Medianero Izquierdo (x): {left_medianero_x}')
print(f'Eje Medianero Derecho (x): {right_medianero_x}')
print(f'Línea Municipal (y): {municipal_line_y}')

# Dibujar las líneas encontradas sobre la imagen
output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# Dibujar los ejes medianeros en la línea municipal
if left_medianero_x != float('inf') and municipal_line_y:
    cv2.line(output_image, (left_medianero_x, municipal_line_y), (left_medianero_x, 0), (0, 255, 0), 2)  # Eje izquierdo en verde
if right_medianero_x != -float('inf') and municipal_line_y:
    cv2.line(output_image, (right_medianero_x, municipal_line_y), (right_medianero_x, 0), (0, 0, 255), 2)  # Eje derecho en rojo

# Dibujar la línea municipal en amarillo, solo entre los ejes medianeros
if left_medianero_x != float('inf') and right_medianero_x != -float('inf') and municipal_line_y:
    cv2.line(output_image, (left_medianero_x, municipal_line_y), (right_medianero_x, municipal_line_y), (0, 255, 255), 2)  # Línea municipal en amarillo

# Guardar la imagen de salida con las líneas destacadas
cv2.imwrite('/home/Maia/planeargas/backend/src/detecciones/ejes_medianeros_municipal.png', output_image)

print('La imagen con los ejes y la línea municipal destacados se ha guardado como ejes_medianeros_municipal.png')
