import cv2
import numpy as np

# Ruta de la imagen de la planta
IMAGEN_PLANTA_PATH = '/home/Maia/planeargas/backend/src/imagen_entrada/planta_1.png'
OUTPUT_TXT_PATH = '/home/Maia/planeargas/backend/src/detecciones/llaves_artefactos.txt'
OUTPUT_LATEX_PATH = '/home/Maia/planeargas/backend/src/detecciones/deteccion_llaves_artefactos.tex'

# Cargar la imagen
imagen_planta = cv2.imread(IMAGEN_PLANTA_PATH)

# Convertir la imagen a espacio de color HSV para detectar el color rojo
hsv = cv2.cvtColor(imagen_planta, cv2.COLOR_BGR2HSV)

# Definir el rango de color rojo para detectar llaves de paso
rojo_bajo1 = np.array([0, 100, 100])
rojo_alto1 = np.array([10, 255, 255])
rojo_bajo2 = np.array([160, 100, 100])
rojo_alto2 = np.array([180, 255, 255])

# Crear dos máscaras para el color rojo
mascara_rojo1 = cv2.inRange(hsv, rojo_bajo1, rojo_alto1)
mascara_rojo2 = cv2.inRange(hsv, rojo_bajo2, rojo_alto2)

# Combinar las dos máscaras
mascara_rojo = mascara_rojo1 | mascara_rojo2

# Encontrar contornos de las llaves de paso (rectángulos rojos)
contornos_llaves, _ = cv2.findContours(mascara_rojo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Lista para almacenar las coordenadas de las llaves
coordenadas_llaves = []

# Filtrar contornos que sean rectángulos y determinar si son llaves de paso
for contorno in contornos_llaves:
    x, y, w, h = cv2.boundingRect(contorno)
    aspect_ratio = float(w) / h
    if 0.2 < aspect_ratio < 5:  # Ajusta los valores para detectar correctamente las llaves de paso
        coordenadas_llaves.append((x + w // 2, y + h // 2))

# Detectar artefactos (color gris)
gris_bajo = np.array([0, 0, 100])
gris_alto = np.array([180, 50, 200])
mascara_gris = cv2.inRange(hsv, gris_bajo, gris_alto)

contornos_artefactos, _ = cv2.findContours(mascara_gris, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Lista para almacenar las coordenadas de los artefactos (centroides)
coordenadas_artefactos = []
for contorno in contornos_artefactos:
    M = cv2.moments(contorno)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        coordenadas_artefactos.append((cx, cy))

# Generar archivo LaTeX para visualizar las llaves de paso y artefactos
with open(OUTPUT_LATEX_PATH, 'w') as f:
    f.write("\\documentclass{article}\n")
    f.write("\\usepackage{tikz}\n")
    f.write("\\begin{document}\n")
    f.write("\\begin{tikzpicture}\n")

    # Graficar artefactos (en gris)
    for artefacto in coordenadas_artefactos:
        f.write(f"\\fill[gray] ({artefacto[0] / 100},{artefacto[1] / 100}) circle (2pt);\n")

    # Graficar llaves de paso (en rojo)
    for llave in coordenadas_llaves:
        f.write(f"\\fill[red] ({llave[0] / 100},{llave[1] / 100}) circle (2pt);\n")

    f.write("\\end{tikzpicture}\n")
    f.write("\\end{document}\n")

print(f"Archivo LaTeX generado: {OUTPUT_LATEX_PATH}")
