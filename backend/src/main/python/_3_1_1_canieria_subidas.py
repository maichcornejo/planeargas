
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


# Función para partir un vector en dos, dado un punto de proyección
def partir_vector(vector, punto_proyeccion):
    (x1, y1), (x2, y2) = vector
    return ((x1, y1), punto_proyeccion), (punto_proyeccion, (x2, y2))

# Función para encontrar el vector más cercano a cada punto
def asignar_punto_a_vector(puntos, vectores):
    vectores_nuevos = []
    asignaciones = []
    puntos.pop(0)
    for vector in vectores:
        (x1, y1), (x2, y2) = vector
        vector_partido = False

        for punto in puntos:
            x, y = punto
            distancia = distancia_punto_vector(x, y, x1, y1, x2, y2)
            distancia_inicio = math.sqrt((x1 - x)**2 + (y1 - y)**2)
            distancia_final = math.sqrt((x2 - x)**2 + (y2 - y)**2)
            
            # Si el punto está en el inicio o final del vector, marcar el vector pero no partir
            if distancia_inicio < 0.01:
                vectores_nuevos.append(vector)
                vectores_nuevos.append(((0, 0), (0, 0)))
                puntos.remove(punto)
                vector_partido = True
                break  # No seguimos procesando más puntos para este vector
            
            # Si la distancia es menor a 0.1, partir el vector
            if distancia < 0.01:
                punto_proyeccion = proyectar_punto_sobre_recta(x, y, x1, y1, x2, y2)
                vector_1, vector_2 = partir_vector(vector, punto_proyeccion)
                vectores_nuevos.append(vector_1)
                vectores_nuevos.append(((0, 0), (0, 0)))  # Indicador
                vectores_nuevos.append(vector_2)
                asignaciones.append((punto, vector, distancia))
                puntos.remove(punto)
                vector_partido = True
                break  # Si partimos el vector, ya no analizamos más puntos para este vector

            if distancia_final < 0.01:
                vectores_nuevos.append(vector)
                vectores_nuevos.append(((0, 0), (0, 0)))
                puntos.remove(punto)
                vector_partido = True
                break  # No seguimos procesando más puntos para este vector

        # Si no se partió el vector ni se detectó punto en el inicio o final, mantenerlo
        if not vector_partido:
            vectores_nuevos.append(vector)
    
    return asignaciones, vectores_nuevos



# Guardar el resultado en un archivo de texto
def guardar_vectores(ruta_salida, vectores):
    with open(ruta_salida, 'w') as archivo:
        for (x1, y1), (x2, y2) in vectores:
            archivo.write(f"\\draw [color=red] ({x1:.2f}, {y1:.2f}) -- ({x2:.2f}, {y2:.2f});\n")


ruta_entrada = "/home/meli/planeargas/backend/src/txt_resultantes/caneria_optimizada.txt"
ruta_salida = "/home/meli/planeargas/backend/src/txt_resultantes/caneria_optimizada_2.txt"
ruta_entrada_saltos = "/home/meli/planeargas/backend/src/txt_resultantes/resultados_subidas_bajadas.txt"

def proceso_principal_subidas(ruta_entrada):
    vectores_troncal = leer_vectores(ruta_entrada)
    subidas = leer_puntos(ruta_entrada_saltos)
    asignaciones,vectores_nuevos = asignar_punto_a_vector(subidas, vectores_troncal)
    guardar_vectores ( ruta_salida, vectores_nuevos)
    # Mostrar los resultados
    for asignacion in asignaciones:
        punto, vector, distancia = asignacion
        print(f"El punto {punto} está más cerca del vector {vector} con una distancia de {distancia:.2f}")

proceso_principal_subidas(ruta_entrada)