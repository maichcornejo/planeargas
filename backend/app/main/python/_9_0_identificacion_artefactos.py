import cv2
import numpy as np
import psycopg2
from math import sqrt

# Clase para representar los artefactos
class Artefacto:
    def __init__(self, id, nombre, orientacion, imagen, x=0, y=0, area=0):
        self.id = id
        self.nombre = nombre
        self.orientacion = orientacion
        self.imagen = imagen  # Imagen en formato binario de la base de datos
        self.x = x
        self.y = y
        self.area = area

# Función para conectar a la base de datos y obtener los artefactos
def obtener_artefactos_desde_bd():
    conn = psycopg2.connect(
        host="localhost",  # Ajusta tu host, usuario, contraseña y base de datos
        database="planeargas",
        user="PLA",
        password="PLA",
        port="28001"
    )
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, orientacion, imagen FROM artefactos")
    
    artefactos = []
    for row in cur.fetchall():
        id, nombre, orientacion, imagen_binaria = row
        # Convertir la imagen binaria en formato numpy para procesarla con OpenCV
        imagen_array = np.frombuffer(imagen_binaria, np.uint8)
        imagen_cv = cv2.imdecode(imagen_array, cv2.IMREAD_COLOR)
        artefacto = Artefacto(id, nombre, orientacion, imagen_cv)
        artefactos.append(artefacto)
    
    cur.close()
    conn.close()
    
    return artefactos

# Función para filtrar artefactos basados en colores
def filtrar_color(imagen, color_bajo, color_alto):
    imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    mascara = cv2.inRange(imagen_hsv, color_bajo, color_alto)
    imagen_filtrada = cv2.bitwise_and(imagen, imagen, mask=mascara)
    
    # Guardar imagen filtrada para depuración
    cv2.imwrite('imagen_filtrada.png', imagen_filtrada)
    
    return imagen_filtrada

def detectar_contornos(imagen):
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    _, umbral = cv2.threshold(imagen_gris, 127, 255, cv2.THRESH_BINARY)
    contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Mostrar cuántos contornos fueron detectados
    print(f"Contornos detectados: {len(contornos)}")
    
    return contornos


# Función para obtener características de los contornos
def obtener_caracteristicas(contorno):
    momentos = cv2.moments(contorno)
    if momentos["m00"] != 0:
        cx = int(momentos["m10"] / momentos["m00"])
        cy = int(momentos["m01"] / momentos["m00"])
    else:
        cx, cy = 0, 0
    area = cv2.contourArea(contorno)
    return cx, cy, area

# Función para comparar imágenes de artefactos con las de la base de datos
def comparar_imagenes(imagen1, imagen2):
    # Redimensionar las imágenes para que coincidan
    imagen1_resized = cv2.resize(imagen1, (imagen2.shape[1], imagen2.shape[0]))
    diferencia = cv2.absdiff(imagen1_resized, imagen2)
    gris = cv2.cvtColor(diferencia, cv2.COLOR_BGR2GRAY)
    _, diferencia_binaria = cv2.threshold(gris, 50, 255, cv2.THRESH_BINARY)
    porcentaje_diferencia = (np.sum(diferencia_binaria) / diferencia_binaria.size) * 100
    return porcentaje_diferencia < 5  # Si la diferencia es menor al 5%, se considera que es el mismo artefacto

# Función para comparar artefactos del plano con los de la base de datos
def comparar_artefactos_plano(imagen_plano, artefactos_bd):
    artefactos_detectados = []
    
    # Definir rangos de color para filtrar (ajustar según el color en las imágenes)
    color_bajo_gris = np.array([0, 0, 50])
    color_alto_gris = np.array([180, 50, 200])

    # Filtrar artefactos en la imagen
    imagen_filtrada = filtrar_color(imagen_plano, color_bajo_gris, color_alto_gris)

    # Detectar contornos en la imagen filtrada
    contornos = detectar_contornos(imagen_filtrada)

    # Iterar sobre cada contorno detectado
    for contorno in contornos:
        cx, cy, area = obtener_caracteristicas(contorno)

        # Extraer el área de interés del plano donde está el artefacto detectado
        x, y, w, h = cv2.boundingRect(contorno)
        artefacto_detectado_img = imagen_plano[y:y+h, x:x+w]

        # Comparar la imagen del artefacto detectado con los artefactos de la base de datos
        for artefacto_bd in artefactos_bd:
            if comparar_imagenes(artefacto_detectado_img, artefacto_bd.imagen):
                artefacto_detectado = Artefacto(artefacto_bd.id, artefacto_bd.nombre, artefacto_bd.orientacion, artefacto_detectado_img, cx, cy, area)
                artefactos_detectados.append(artefacto_detectado)

    return artefactos_detectados

# Función para generar el archivo de reporte
def generar_reporte(artefactos_detectados):
    with open('resultado.txt', 'w') as archivo:
        for artefacto in artefactos_detectados:
            archivo.write(f"{artefacto.nombre}, {artefacto.orientacion}, ({artefacto.x}, {artefacto.y})\n")

# Función para dibujar los artefactos identificados en la imagen
def dibujar_artefactos(imagen, artefactos):
    for artefacto in artefactos:
        cv2.putText(imagen, artefacto.nombre, (artefacto.x, artefacto.y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    cv2.imwrite('resultado_imagen.png', imagen)

# Cargar la imagen del plano (asegúrate de tener la ruta correcta)
imagen_plano = cv2.imread('/home/Maia/planeargas/backend/app/imagen_entrada/planta_1.png')

# Obtener los artefactos desde la base de datos
artefactos_base_datos = obtener_artefactos_desde_bd()

# Comparar artefactos del plano con los de la base de datos
artefactos_detectados = comparar_artefactos_plano(imagen_plano, artefactos_base_datos)

# Generar el reporte en un archivo de texto
generar_reporte(artefactos_detectados)

# Dibujar los artefactos identificados en la imagen
dibujar_artefactos(imagen_plano, artefactos_detectados)

print("Comparación finalizada. Resultados guardados en 'resultado.txt' y 'resultado_imagen.png'.")
