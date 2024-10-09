import cv2
import numpy as np

def es_rejilla(contour, hsv_image, mask):
    x, y, w, h = cv2.boundingRect(contour)
    aspect_ratio = w / float(h)

    # Ajustar el rango del aspect ratio para rejillas más cuadradas o ligeramente rectangulares
    if 0.5 < aspect_ratio < 1.5 and 10 < w < 50 and 10 < h < 50:
        # Aproximar el contorno para verificar que tenga 4 lados (rectángulo)
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if len(approx) == 4:
            # Calcular el centroide del contorno
            M = cv2.moments(contour)
            if M['m00'] != 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])

                # Definir una región para buscar píxeles verdes a los lados (para ventilaciones)
                side_width = w // 4  # Ajustar según el tamaño de la rejilla
                side_height = h
                left_side = hsv_image[cy - side_height//2: cy + side_height//2, cx - w//2 - side_width: cx - w//2]
                right_side = hsv_image[cy - side_height//2: cy + side_height//2, cx + w//2: cx + w//2 + side_width]

                # Definir el rango de color verde
                lower_green = np.array([40, 40, 40])
                upper_green = np.array([70, 255, 255])

                # Crear máscaras para los lados
                mask_left = cv2.inRange(left_side, lower_green, upper_green)
                mask_right = cv2.inRange(right_side, lower_green, upper_green)

                # Contar los píxeles verdes en ambos lados
                green_pixels_left = cv2.countNonZero(mask_left)
                green_pixels_right = cv2.countNonZero(mask_right)

                # Si ambos lados tienen pocos píxeles verdes, es una rejilla
                if green_pixels_left < 500 and green_pixels_right < 500:  # Ajustar umbral según necesidad
                    return True

    return False

# Cargar la imagen
image_path = '/home/Maia/planeargas/backend/app/imagen_entrada/planta_3.png'
image = cv2.imread(image_path)

# Convertir la imagen a formato HSV (para detección de color)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Definir el rango de color para detectar el verde (para las ventilaciones resaltadas en verde)
lower_green = np.array([40, 40, 40])
upper_green = np.array([70, 255, 255])

# Crear una máscara que detecte solo los píxeles en el rango verde
mask_green = cv2.inRange(hsv_image, lower_green, upper_green)

# Aplicar operaciones morfológicas para eliminar ruido y mejorar la detección de contornos
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mask_clean = cv2.morphologyEx(mask_green, cv2.MORPH_CLOSE, kernel, iterations=2)
mask_clean = cv2.morphologyEx(mask_clean, cv2.MORPH_OPEN, kernel, iterations=2)

# Encontrar los contornos en la máscara limpia
contours, _ = cv2.findContours(mask_clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

rejillas = []
for contour in contours:
    if es_rejilla(contour, hsv_image, mask_clean):
        # Calcular el centroide de cada rejilla
        M = cv2.moments(contour)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])  # Coordenada X
            cy = int(M['m01'] / M['m00'])  # Coordenada Y
            rejillas.append((cx, cy))

            # Dibujar un círculo en el centro de la rejilla detectada (color blanco en formato BGR)
            cv2.circle(image, (cx, cy), 5, (255, 255, 255), -1)

# Guardar la imagen con las rejillas detectadas
output_image_path = '/home/Maia/planeargas/backend/app/detecciones/plano_con_rejillas.png'
cv2.imwrite(output_image_path, image)

# Generar el archivo de texto con las coordenadas
output_txt_path = '/home/Maia/planeargas/backend/app/detecciones/ubicacion_rejillas.txt'
with open(output_txt_path, 'w') as file:
    for i, (cx, cy) in enumerate(rejillas):
        file.write(f"Rejilla {i + 1}: X = {cx}, Y = {cy}\n")

print(f"Imagen guardada en: {output_image_path}")
print(f"Coordenadas guardadas en: {output_txt_path}")
