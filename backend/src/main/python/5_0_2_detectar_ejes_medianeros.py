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
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=50, maxLineGap=5)

# Inicializar variables para almacenar las coordenadas de los ejes medianeros
left_medianero_x = float('inf')  # La coordenada x más pequeña
right_medianero_x = -float('inf')  # La coordenada x más grande
municipal_line_y = None

# Iterar sobre las líneas detectadas
for line in lines:
    x1, y1, x2, y2 = line[0]
    
    # Si la línea es vertical (misma coordenada x con margen de error)
    if abs(x1 - x2) < 10:
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

# Calcular la longitud en píxeles de la línea municipal
if left_medianero_x != float('inf') and right_medianero_x != -float('inf'):
    longitud_municipal_pixels = right_medianero_x - left_medianero_x
    print(f'La línea municipal mide {longitud_municipal_pixels} píxeles en el plano.')

# Obtener la escala metros por píxel usando un plano de referencia con longitud real
longitud_real_metros = 15.65  # Ejemplo, solo en plano de referencia
escala_metros_por_pixel = longitud_real_metros / longitud_municipal_pixels
print(f'La escala es de {escala_metros_por_pixel:.5f} metros por píxel.')

# Calcular la longitud en metros de la línea municipal
longitud_municipal_metros = longitud_municipal_pixels * escala_metros_por_pixel
print(f'La línea municipal mide {longitud_municipal_metros:.2f} metros.')

# Guardar la imagen con los ejes y la línea municipal dibujada
output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# Dibujar los ejes medianeros y la línea municipal
if left_medianero_x != float('inf') and municipal_line_y:
    cv2.line(output_image, (left_medianero_x, municipal_line_y), (left_medianero_x, 0), (0, 255, 0), 2)  # Eje izquierdo en verde
if right_medianero_x != -float('inf') and municipal_line_y:
    cv2.line(output_image, (right_medianero_x, municipal_line_y), (right_medianero_x, 0), (0, 0, 255), 2)  # Eje derecho en rojo

if left_medianero_x != float('inf') and right_medianero_x != -float('inf') and municipal_line_y:
    cv2.line(output_image, (left_medianero_x, municipal_line_y), (right_medianero_x, municipal_line_y), (0, 255, 255), 2)  # Línea municipal en amarillo

cv2.imwrite('/home/Maia/planeargas/backend/src/detecciones/ejes_medianeros_municipal_con_escala.png', output_image)

# Guardar los datos en un archivo txt
txt_output_path = '/home/Maia/planeargas/backend/src/detecciones/resultado_ejes_municipal.txt'
with open(txt_output_path, 'w') as f:
    f.write(f'Eje Medianero Izquierdo (X): {left_medianero_x} px\n')
    f.write(f'Eje Medianero Derecho (X): {right_medianero_x} px\n')
    f.write(f'Longitud del Eje Municipal en Píxeles: {longitud_municipal_pixels} px\n')
    f.write(f'Longitud del Eje Municipal en Metros: {longitud_municipal_metros:.2f} m\n')

print(f'Los datos se han guardado en {txt_output_path}')
