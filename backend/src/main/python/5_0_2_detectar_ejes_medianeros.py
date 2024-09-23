import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
image_path = '/mnt/data/paredes.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Detectar bordes usando Canny
edges = cv2.Canny(image, threshold1=100, threshold2=200)

# Encontrar las coordenadas no cero (donde hay líneas)
coordinates = np.column_stack(np.where(edges > 0))

# Obtener los puntos más a la izquierda y más a la derecha (en el eje X)
left_medianero = coordinates[np.argmin(coordinates[:, 1])]
right_medianero = coordinates[np.argmax(coordinates[:, 1])]

# Asumimos que 1 pixel = 1 metro para este ejemplo (modificar esta parte si se tiene otra escala)
# Si se tiene una escala, reemplazar esta parte por la conversión adecuada
pixels_to_meters = 1  # Cambiar si hay una escala diferente

# Calcular las posiciones en metros
left_medianero_meters = left_medianero[1] * pixels_to_meters
right_medianero_meters = right_medianero[1] * pixels_to_meters

# Guardar los resultados en un archivo de texto
output_txt = '/home/Maia/planeargas/backend/src/imagen_salida/paredes.png'
with open(output_txt, "w") as f:
    f.write(f"Eje medianero izquierdo en pixeles: {left_medianero[1]}\n")
    f.write(f"Eje medianero derecho en pixeles: {right_medianero[1]}\n")
    f.write(f"Eje medianero izquierdo en metros: {left_medianero_meters}\n")
    f.write(f"Eje medianero derecho en metros: {right_medianero_meters}\n")

# Marcar los puntos sobre la imagen original
marked_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.circle(marked_image, (left_medianero[1], left_medianero[0]), 10, (0, 0, 255), -1)
cv2.circle(marked_image, (right_medianero[1], right_medianero[0]), 10, (0, 0, 255), -1)

# Guardar la nueva imagen con los puntos marcados
output_image_path = "/mnt/data/marked_medianeros.png"
cv2.imwrite(output_image_path, marked_image)

# Mostrar la imagen con los puntos marcados
plt.imshow(cv2.cvtColor(marked_image, cv2.COLOR_BGR2RGB))
plt.show()

print(f"Proceso completado. Resultados guardados en {output_txt} y {output_image_path}")
