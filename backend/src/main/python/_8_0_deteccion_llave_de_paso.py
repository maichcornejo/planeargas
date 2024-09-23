import cv2
import numpy as np

# Cargar la imagen principal (cañería) y la plantilla (llave de paso)
image_path = '/mnt/data/planta1.PNG'
template_path = '/mnt/data/llave.png'

image = cv2.imread(image_path)
template = cv2.imread(template_path, 0)  # Leer la plantilla en escala de grises

# Escalar la plantilla para adaptarse mejor a la imagen principal si es necesario
scale_factor = 1.5  # Puedes ajustar este valor
template = cv2.resize(template, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

# Convertir la imagen principal a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Obtener las dimensiones de la plantilla
w, h = template.shape[::-1]

# Aplicar matchTemplate para encontrar las coincidencias
result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)

# Definir un umbral de coincidencia (se puede ajustar)
threshold = 0.7  # Ajustar el valor para más o menos coincidencias
loc = np.where(result >= threshold)

# Inicializar una lista para las coordenadas de las llaves de paso
llaves_de_paso = []

# Dibujar rectángulos donde se encuentran las coincidencias y guardar las coordenadas
for pt in zip(*loc[::-1]):
    # Dibujar un rectángulo en la imagen principal para marcar la coincidencia
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
    llaves_de_paso.append((pt[0], pt[1], pt[0] + w, pt[1] + h))

# Guardar la imagen con las llaves de paso detectadas para verificación
cv2.imwrite('/mnt/data/llaves_de_paso_detectadas.png', image)

# Exportar las coordenadas de las llaves de paso a un archivo de texto
with open('/mnt/data/deteccion_llaves_de_paso.txt', 'w') as file:
    for llave in llaves_de_paso:
        file.write(f"Llave de paso en coordenadas: {llave[0]}, {llave[1]} a {llave[2]}, {llave[3]}\n")

print("Detección completada. Coordenadas exportadas.")
