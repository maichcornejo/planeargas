import numpy as np
import re
from shapely.geometry import LineString, MultiLineString

def calcular_centroide_vectores(vectores):
    if len(vectores) == 0:
        raise ValueError("La lista de vectores está vacía")

    puntos_medios = []
    
    # Calculamos los puntos medios de cada vector
    for (xi, yi), (xf, yf) in vectores:
        punto_medio = ((xi + xf) / 2, (yi + yf) / 2)
        puntos_medios.append(punto_medio)
    
    # Convertimos a un array de NumPy para facilitar el cálculo
    matriz_puntos_medios = np.array(puntos_medios)
    
    # Calculamos el centroide (promedio de los puntos medios)
    centroide = np.mean(matriz_puntos_medios, axis=0)
    
    return centroide

def leer_vectores(ruta_archivo):
    vectores = []
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Extraer coordenadas de los vectores usando expresiones regulares
            coordenadas = re.findall(r"\(([-\d.eE]+), ([-\d.eE]+)\) -- \(([-\d.eE]+), ([-\d.eE]+)\)", linea)
            if coordenadas:
                x1, y1, x2, y2 = map(float, coordenadas[0])
                vectores.append(((x1, y1), (x2, y2)))
    return vectores


def sumar_vectores(vector1, vector2):
    # Extraer las coordenadas de los vectores
    x1, y1 = vector1
    x2, y2 = vector2
    
    # Sumar las componentes correspondientes
    resultado_x = x1 + x2
    resultado_y = y1 + y2
    
    # Devolver el vector resultante
    return (resultado_x, resultado_y)

def sumar_muchos_vectores(vectores, vector, ruta_salida, color):
    if len(vectores) == 0:
        raise ValueError("La lista de vectores está vacía")

    nuevos_vectores = []
    x, y = vector
    # Calculamos los puntos desplazados de cada vector
    for (xi, yi), (xf, yf) in vectores:
        inicial = (xi + x, yi + y)
        final = (xf + x, yf + y)
        line_string = LineString([inicial, final])
        nuevos_vectores.append((line_string))
    
        # Exportar a archivo txt con formato LaTeX
    with open(ruta_salida, 'w') as f:
        for vector in nuevos_vectores:
            if isinstance(vector, MultiLineString):
                for line in vector:
                    coords = list(line.coords)
                    for i in range(len(coords) - 1):
                        x1, y1 = coords[i]
                        x2, y2 = coords[i + 1]
                        f.write(f'\\draw [color={color}] ({x1:.2f}, {y1:.2f}) -- ({x2:.2f}, {y2:.2f});\n')
            else:
                coords = list(vector.coords)
                for i in range(len(coords) - 1):
                    x1, y1 = coords[i]
                    x2, y2 = coords[i + 1]
                    f.write(f'\\draw [color={color}] ({x1:.2f}, {y1:.2f}) -- ({x2:.2f}, {y2:.2f});\n')

    return nuevos_vectores


ruta_salida = '/home/meli/planeargas/backend/src/txt_resultantes/restados.txt'
color = 'red'
vector_1 = (8.46, 8.24)
vectores = leer_vectores('/home/meli/planeargas/backend/src/txt_resultantes/centroides.txt')
# centroide = calcular_centroide_vectores(vectores)
#centroide = (-6.105,-5.30)
#punto_final = sumar_vectores (centroide,vector_1)
sumar_muchos_vectores(vectores, vector_1, ruta_salida, color)
#print(centroide)