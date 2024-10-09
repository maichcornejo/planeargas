from _3_1_0_normalizar_vectores import optimizar_caneria
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
def asignar_punto_a_vector(vectores_1, vectores):
    vectores_nuevos = []
    asignaciones = []
    for vector in vectores:
        (x1, y1), (x2, y2) = vector
        vector_partido = False
        for punto in vectores_1: 
            for vec in punto:
                x, y = vec
                distancia = distancia_punto_vector(x, y, x1, y1, x2, y2)
                distancia_inicio = math.sqrt((x1 - x)**2 + (y1 - y)**2)
                distancia_final = math.sqrt((x2 - x)**2 + (y2 - y)**2)
                
                # Si el punto está en el inicio o final del vector, marcar el vector pero no partir
                if distancia_inicio < 0.01 and not vector_partido:
                    vectores_nuevos.append(vector)
                    vectores_nuevos.append(((10, 10), (10, 10)))
                    vectores_1.remove(punto)
                    vector_partido = True
                    break  # No seguimos procesando más puntos para este vector
                
                # Si la distancia es menor a 0.1, partir el vector
                if distancia < 0.01 and not vector_partido:
                    punto_proyeccion = proyectar_punto_sobre_recta(x, y, x1, y1, x2, y2)
                    vector_1, vector_2 = partir_vector(vector, punto_proyeccion)
                    vectores_nuevos.append(vector_1)
                    vectores_nuevos.append(((10, 10), (10, 10)))  # Indicador
                    vectores_nuevos.append(vector_2)
                    asignaciones.append((punto, vector, distancia))
                    vectores_1.remove(punto)
                    vector_partido = True
                    break  # Si partimos el vector, ya no analizamos más puntos para este vector

                if distancia_final < 0.01 and not vector_partido:
                    vectores_nuevos.append(vector)
                    vectores_nuevos.append(((10, 10), (10, 10)))
                    vectores_1.remove(punto)
                    vector_partido = True
                    break  # No seguimos procesando más puntos para este vector
            
            # Si no se partió el vector ni se detectó punto en el inicio o final, mantenerlo
            if not vector_partido:
                vectores_nuevos.append(vector)
        
    return asignaciones, vectores_nuevos



def encontrar_vector_mas_proximo(vectores_1, vectores_2):
    vector_mas_proximo_1 = None
    vector_mas_proximo_2 = None
    distancia_minima = float('inf')  # Inicializamos la distancia mínima como infinita

    for v1 in vectores_1:
        (px1,py1), (px2, py2) = v1
        for v2 in vectores_2:
            (x1, y1), (x2, y2) = v2
            distancia_1 = distancia_punto_vector(px1, py1, x1, y1, x2, y2)
            distancia_2 = distancia_punto_vector(px2, py2, x1, y1, x2, y2)
            if distancia_1 < distancia_minima:
                distancia_minima = distancia_1
                vector_mas_proximo_2 = v2
                vector_mas_proximo_1 = v1
            if distancia_2 < distancia_minima:
                distancia_minima = distancia_2
                vector_mas_proximo_2 = v2
                vector_mas_proximo_1 = v1
    return vector_mas_proximo_2,vector_mas_proximo_1, distancia_minima

# Guardar el resultado en un archivo de texto
def guardar_vectores(ruta_salida, vectores):
    with open(ruta_salida, 'w') as archivo:
        for (x1, y1), (x2, y2) in vectores:
            archivo.write(f"\\draw [color=red] ({x1:.2f}, {y1:.2f}) -- ({x2:.2f}, {y2:.2f});\n")


ruta_entrada_todos = "/home/meli/planeargas/backend/src/txt_resultantes/resultados_caneria_latex.txt"
ruta_entrada_troncal = "/home/meli/planeargas/backend/src/txt_resultantes/caneria_optimizada.txt"
ruta_salida = "/home/meli/planeargas/backend/src/txt_resultantes/caneria_optimizada_3.txt"

def proceso_principal_artefactos(ruta_entrada_todos,ruta_entrada_troncal):
    vectores_todos = leer_vectores(ruta_entrada_todos)
    vectores_troncal = leer_vectores(ruta_entrada_troncal)
    vectores_resta = list(set(vectores_todos) - set(vectores_troncal))
    guardar_vectores(ruta_salida, vectores_resta)
    optimizar_caneria(ruta_salida,ruta_salida)
    asignaciones, vectores_nuevos = asignar_punto_a_vector(vectores_resta, vectores_troncal)
        # Mostrar los resultados
    for asignacion in asignaciones:
        punto, vector, distancia = asignacion
        print(f"El punto {punto} está más cerca del vector {vector} con una distancia de {distancia:.2f}")
    guardar_vectores(ruta_salida, vectores_nuevos)

proceso_principal_artefactos(ruta_entrada_todos,ruta_entrada_troncal)