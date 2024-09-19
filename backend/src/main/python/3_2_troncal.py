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

def dibujar_linea(x_real, y_real, distancia, angulo_grados, negativo_x, negativo_y):
    angulo_radianes = math.radians(angulo_grados)
    longitud = (abs(distancia * math.cos(angulo_radianes)))*negativo_x + x_real
    altura = (abs(distancia * math.sin(angulo_radianes)))*negativo_y + y_real
    return longitud, altura, f"\\draw [color=red] ({x_real:.1f}, {y_real:.1f}) -- ({longitud:.1f}, {altura:.1f});"


def isometrica(vectores):
    primer_vector = vectores[0]
    vector_actual = vectores[1]
    (pv_x2, pv_y2) = primer_vector[1]
    (va_x1, va_y1), (va_x2, va_y2) = vector_actual
    distancia = math.sqrt((va_x2 - va_x1)**2 + (va_y2 - va_y1)**2)
    
    if va_x1 == va_x2:
        if va_y1 < va_y2:
            punto_actual = (va_x2, va_y2)
        else:
            punto_actual = (va_x1, va_y1)
        resultados = ["\\draw [color=red] (0, 0) -- (0, 0.2) -- (.5, .5) -- (.5, -2);"]
        x_real, y_real = .5, -2
    else:
        distancia_1 = math.sqrt((pv_x2 - va_x1)**2 + (pv_y2 - va_y1)**2)
        distancia_2 = math.sqrt((pv_x2 - va_x2)**2 + (pv_y2 - va_y2)**2)
        if distancia_1 > distancia_2:
            punto_actual = (va_x1, va_y1)
        else:
            punto_actual = (va_x2, va_y2)
        
        if ((va_x1 + va_x2) / 2) > pv_x2:
            # derecha 
            resultados = ["\\draw [color=red] (0, 0) -- (0, 0.2) -- (.5, -0.2) -- (.5, -2);"]
            x_real, y_real = .5, -2
        else:
            # izquierda 
            resultados = ["\\draw [color=red] (0, 0) -- (0, 0.2) -- (-.5, .5) -- (-.5, -2);"]
            x_real, y_real = -.5, -2

    # Decidir el índice de inicio del bucle según la distancia
    if distancia > 0.5:
        inicio_bucle = 1
    else:
        inicio_bucle = 2

    # siguiente vector
    for vector_siguiente in vectores[inicio_bucle:]:
        (vs_x1, vs_y1), (vs_x2, vs_y2) = vector_siguiente
        (pa_x, pa_y) = punto_actual
        distancia = min(10, max(1, abs(vs_y2 - vs_y1 if vs_x1 == vs_x2 else vs_x2 - vs_x1)))
        if vs_x1 == vs_x2:
            angulo = 30
            if ((vs_y1 + vs_y2) / 2) > pa_y:
                # izquierda
                x_real, y_real, linea = dibujar_linea(x_real, y_real, distancia, angulo, -1, -1)
            else:
                # derecha
                x_real, y_real, linea = dibujar_linea(x_real, y_real, distancia, angulo, 1, 1)
        else:
            angulo = 150
            if ((vs_x1 + vs_x2) / 2) > pa_x:
                # izquierda
                x_real, y_real, linea = dibujar_linea(x_real, y_real, distancia, angulo, -1, 1)
            else:
                # derecha
                x_real, y_real, linea = dibujar_linea(x_real, y_real, distancia, angulo, 1, -1)
        
        resultados.append(linea)
        distancia_1 = math.sqrt((pa_x - vs_x1)**2 + (pa_y - vs_y1)**2)
        distancia_2 = math.sqrt((pa_x - vs_x2)**2 + (pa_y - vs_y2)**2)
        
        if distancia_1 > distancia_2:
            punto_actual = (vs_x1, vs_y1)
        else:
            punto_actual = (vs_x2, vs_y2)
    
    return resultados


    
def optimizar_caneria(ruta_entrada, ruta_salida):
    vectores = leer_vectores(ruta_entrada)
    resultados = isometrica(vectores)
    
    with open(ruta_salida, 'w') as archivo:
        for linea in resultados:
            archivo.write(linea + '\n')

# Ruta de los archivos
ruta_entrada = "/home/meli/planeargas/PlaneArGas/backend/src/txt_resultantes/caneria_optimizada.txt"
ruta_salida = "/home/meli/planeargas/PlaneArGas/backend/src/txt_resultantes/troncal_latex.txt"

# Ejecutar el proceso de optimización con proyección
optimizar_caneria(ruta_entrada, ruta_salida)
