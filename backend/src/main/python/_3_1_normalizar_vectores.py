import re
import math

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


# Ordenar los vectores por el valor 'y' mayor de cada par
def ordenar_vectores_por_y(vectores):
    return sorted(vectores, key=lambda v: max(v[0][1], v[1][1]), reverse=True)


def proyectar_y_conectar_vectores(vectores):
    cadena_vectores = []
    # Tomar el primer vector como punto inicial
    cadena_vectores.append(vectores[0])
    punto_1, punto_2 = vectores[0]
    vectores.remove(cadena_vectores[0])

    # Determinar cuál punto tiene menor coordenada y tomarlo como punto inicial
    if punto_1[1] > punto_2[1]:
        punto_actual = punto_2
    else:
        punto_actual = punto_1

    while vectores:  # Iterar mientras queden vectores por conectar
        vector_mas_cercano = None
        distancia_minima = float('inf')  # Iniciar con un valor muy grande

        # Buscar el vector más cercano comparando ambos puntos de cada vector
        for vector in vectores:
            p1, p2 = vector

            # Comparar distancias del punto_actual a los dos puntos del vector
            distancia_p1 = math.sqrt((punto_actual[0] - p1[0])**2 + (punto_actual[1] - p1[1])**2)
            distancia_p2 = math.sqrt((punto_actual[0] - p2[0])**2 + (punto_actual[1] - p2[1])**2)

            # Revisar si cualquiera de los dos puntos es más cercano
            if distancia_p1 < distancia_minima:
                distancia_minima = distancia_p1
                vector_mas_cercano = vector
                punto_mas_lejano = p2
            if distancia_p2 < distancia_minima:
                distancia_minima = distancia_p2
                vector_mas_cercano = vector
                punto_mas_lejano = p1

        # Añadir el vector más cercano a la cadena y actualizar el punto actual
        if vector_mas_cercano is not None:
            print(distancia_minima)
            if distancia_minima > 0.17:
                break
            else:
                vectores.remove(vector_mas_cercano)
                cadena_vectores.append(vector_mas_cercano)
                # Actualizar el punto_actual al punto más cercano del vector seleccionado
                punto_actual = punto_mas_lejano

        else:
            # Si no se encuentra vector cercano, se rompe el bucle
            break

    return cadena_vectores


def borrar_llaves(vectores):
    vectores_filtrados = []
    for (x1, y1), (x2, y2) in vectores:
        numero_truncado = abs(float(format((x1 - x2) + (y1 - y2), ".2f")))
        if numero_truncado > 0.11:
            vectores_filtrados.append(((x1, y1), (x2, y2)))
    return vectores_filtrados



# Guardar el resultado en un archivo de texto
def guardar_vectores(ruta_salida, vectores):
    with open(ruta_salida, 'w') as archivo:
        for (x1, y1), (x2, y2) in vectores:
            archivo.write(f"\\draw [color=red] ({x1}, {y1}) -- ({x2}, {y2});\n")

# Proceso principal
def optimizar_caneria(ruta_entrada, ruta_salida):
    vectores = leer_vectores(ruta_entrada)
    vectores_ordenados = ordenar_vectores_por_y(vectores)
    vectores_sin_llaves = borrar_llaves(vectores_ordenados)
    vectores_proyectados = proyectar_y_conectar_vectores(vectores_ordenados)
    guardar_vectores(ruta_salida, vectores_proyectados)


# Ruta de los archivos
ruta_entrada = "/home/meli/planeargas/backend/src/txt_resultantes/resultados_caneria_latex.txt"
ruta_salida = "/home/meli/planeargas/backend/src/txt_resultantes/caneria_optimizada.txt"

# Ejecutar el proceso de optimización con proyección
optimizar_caneria(ruta_entrada, ruta_salida)
