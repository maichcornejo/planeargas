
import re
import math
import os

# Leer los vectores del archivo de entrada
def leer_vectores(ruta_archivo):
    vectores = []
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Extraer coordenadas de los vectores
            coordenadas = re.findall(r"\(([\d.]+), ([\d.]+)\) -- \(([\d.]+), ([\d.]+)\)", linea)
            if coordenadas:
                x1, y1, x2, y2 = map(float, coordenadas[0])
                vectores.append(((x1, y1), (x2, y2)))
    return vectores

# Método para leer los puntos desde el archivo
def leer_puntos(ruta_archivo):
    puntos = []
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Usar expresión regular para extraer los puntos del formato LaTeX
            coordenadas = re.findall(r"\(([\d.]+), ([\d.]+)\)", linea)
            if coordenadas:
                for coord in coordenadas:
                    x, y = map(float, coord)
                    puntos.append((x, y))
    return puntos

import math

# Función para encontrar la distancia del punto a la recta
def distancia_punto_vector(px, py, x1, y1, x2, y2):
    numerador = abs((y2 - y1) * px - (x2 - x1) * py + x2 * y1 - y2 * x1)
    denominador = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
    return numerador / denominador

# Función para proyectar un punto sobre una recta
def proyectar_punto_sobre_recta(px, py, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0 and dy == 0:
        return (x1, y1)  # Los dos puntos son iguales, la recta no existe realmente.

    # Proyección del punto sobre la recta
    t = ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)
    
    # Calcular las coordenadas del punto proyectado
    punto_proyectado_x = x1 + t * dx
    punto_proyectado_y = y1 + t * dy
    
    return (punto_proyectado_x, punto_proyectado_y)

# Función para encontrar el vector más cercano a cada punto
def asignar_punto_a_vector(puntos, vectores):
    puntos.pop(0)
    vectores_nuevos = []
    asignaciones = []

    for punto in puntos:
        x, y = punto
        distancia_minima = float('inf')
        vector_mas_cercano = None
        punto_proyeccion = None

        for vector in vectores:
            (x1, y1), (x2, y2) = vector
            # Calcular la distancia del punto al vector
            distancia = distancia_punto_vector(x, y, x1, y1, x2, y2)
            distancia_inicio = math.sqrt((x2 - x)**2 + (y2 - y)**2)
            #if distancia_inicio < 0.05:
                
            # Si la distancia es menor que la distancia mínima actual, actualizamos
            if distancia < distancia_minima:
                distancia_minima = distancia
                vector_mas_cercano = vector
                # Encontrar el punto proyectado más cercano en la recta
                punto_proyeccion = proyectar_punto_sobre_recta(x, y, x1, y1, x2, y2)
                print(f"Distancia mínima: {distancia_minima}, Punto proyectado: {punto_proyeccion}")

        # Solo partir el vector si la distancia mínima es menor a 0.1
        if distancia_minima < 0.1:
            vectores.remove(vector)
            if punto_proyeccion:
                vector_1, vector_2 = partir_vector(vector_mas_cercano, punto_proyeccion)
                vectores_nuevos.append(vector_1)
                vectores_nuevos.append(((0, 0),(0,0)))
                vectores_nuevos.append(vector_2)
            asignaciones.append((punto, vector_mas_cercano, distancia_minima))
        else:
            print(f"El punto {punto} no se usa para partir el vector, ya que la distancia es mayor a 0.1")

    return asignaciones, vectores_nuevos

# Función para partir un vector dado un punto de división
def partir_vector(vector, punto):
    (x1, y1), (x2, y2) = vector
    (px, py) = punto
    
    # Crea los dos nuevos vectores
    vector1 = ((x1, y1), (px, py))
    vector2 = ((px, py), (x2, y2))
    
    return vector1, vector2



# Guardar el resultado en un archivo de texto
def guardar_vectores(ruta_salida, vectores):
    with open(ruta_salida, 'w') as archivo:
        for (x1, y1), (x2, y2) in vectores:
            archivo.write(f"\\draw [color=red] ({x1:.2f}, {y1:.2f}) -- ({x2:.2f}, {y2:.2f});\n")


ruta_entrada = "/home/meli/planeargas/backend/src/txt_resultantes/caneria_optimizada.txt"
ruta_salida = "/home/meli/planeargas/backend/src/txt_resultantes/caneria_optimizada_2.txt"
ruta_entrada_saltos = "/home/meli/planeargas/backend/src/txt_resultantes/resultados_subidas_bajadas.txt"

def proceso_principal(ruta_entrada):
    vectores_troncal = leer_vectores(ruta_entrada)
    subidas = leer_puntos(ruta_entrada_saltos)
    asignaciones,vectores_nuevos = asignar_punto_a_vector(subidas, vectores_troncal)
    vectores_totales = vectores_troncal+vectores_nuevos
    guardar_vectores ( ruta_salida, vectores_totales)
    # Mostrar los resultados
    for asignacion in asignaciones:
        punto, vector, distancia = asignacion
        print(f"El punto {punto} está más cerca del vector {vector} con una distancia de {distancia:.2f}")

proceso_principal(ruta_entrada)