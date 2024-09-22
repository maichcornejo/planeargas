import cv2
import numpy as np
from PIL import Image, ImageDraw

# Cargar imagen del plano en formato PNG
imagen = cv2.imread('/home/Maia/planeargas/backend/src/imagen_salida/paredes.png')

# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar un umbral para destacar el medidor (rectángulo)
_, umbral = cv2.threshold(imagen_gris, 200, 255, cv2.THRESH_BINARY_INV)

# Encontrar contornos en la imagen
contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Variables para almacenar la coordenada del medidor
coordenadas_medidor = None
dimension_medidor_px = None

# Definir dimensiones del medidor en metros y el factor de conversión a píxeles (asumido)
dim_medidor_metros = (0.40, 0.30)
escala = 100  # Número de píxeles por metro (ajustar según escala del plano)

# Buscar el rectángulo que corresponda al medidor
for contorno in contornos:
    x, y, w, h = cv2.boundingRect(contorno)
    width_m, height_m = w / escala, h / escala  # Convertir de píxeles a metros
    
    if abs(width_m - dim_medidor_metros[0]) < 0.05 and abs(height_m - dim_medidor_metros[1]) < 0.05:
        coordenadas_medidor = (x, y)
        dimension_medidor_px = (w, h)
        break

if coordenadas_medidor:
    x_medidor, y_medidor = coordenadas_medidor
    print(f"Medidor encontrado en coordenadas (x: {x_medidor}, y: {y_medidor}) en píxeles.")

    # Guardar las coordenadas en un archivo .txt
    with open("coordenadas_medidor.txt", "w") as archivo:
        archivo.write(f"Medidor de gas ubicado en:\n")
        archivo.write(f"Coordenadas (en píxeles): {x_medidor}, {y_medidor}\n")
        archivo.write(f"Dimensiones (en píxeles): {dimension_medidor_px[0]} x {dimension_medidor_px[1]}")

    # Convertir la imagen de OpenCV (BGR) a formato RGB para Pillow
    imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    imagen_pillow = Image.fromarray(imagen_rgb)

    # Crear un objeto para dibujar sobre la imagen
    draw = ImageDraw.Draw(imagen_pillow)

    # Dibujar un rectángulo donde está el medidor
    draw.rectangle([x_medidor, y_medidor, x_medidor + dimension_medidor_px[0], y_medidor + dimension_medidor_px[1]], outline="red", width=3)

    # Guardar la imagen con el rectángulo del medidor marcado
    imagen_pillow.save("plano_con_medidor.png")
    print("Imagen guardada como 'plano_con_medidor.png'.")
    
    # Generar archivo LaTeX para visualización gráfica
    with open("ubicacion_medidor.tex", "w") as archivo_latex:
        archivo_latex.write(r"\documentclass{article}" + "\n")
        archivo_latex.write(r"\usepackage{tikz}" + "\n")
        archivo_latex.write(r"\begin{document}" + "\n")
        archivo_latex.write(r"\begin{tikzpicture}" + "\n")
        
        # Dibujar el plano de fondo (esquemático)
        archivo_latex.write(f"\\draw[step=1cm,gray,very thin] (0,0) grid ({imagen.shape[1]/escala}m,{imagen.shape[0]/escala}m);\n")
        
        # Dibujar el medidor como un rectángulo
        archivo_latex.write(f"\\filldraw[fill=blue!20] ({x_medidor/escala},{y_medidor/escala}) rectangle "
                            f"({(x_medidor + dimension_medidor_px[0])/escala},{(y_medidor + dimension_medidor_px[1])/escala});\n")
        
        archivo_latex.write(r"\end{tikzpicture}" + "\n")
        archivo_latex.write(r"\end{document}" + "\n")

    print("Archivos .txt y .tex generados correctamente.")
else:
    print("Medidor no encontrado en la imagen.")
