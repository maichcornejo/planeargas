from _8_artefactos import menu_principal
import re
import math
import os

numero = 0.65

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


def dibujar_linea(x_real, y_real, distancia, angulo_grados, negativo_x, negativo_y,longitud_real,tipo_caneria,tipo_caneria_abreviado):
            distancia = distancia * 2
            angulo_radianes = math.radians(angulo_grados)
            longitud = (abs(distancia * math.cos(angulo_radianes)))*negativo_x + x_real
            altura = (abs(distancia * math.sin(angulo_radianes)))*negativo_y + y_real
            if angulo_grados == 150:
                angulo_grados = -30
            ubi_texto_x = ((x_real + longitud) / 2)
            ubi_texto_y = ((y_real + altura) / 2)+.25
            linea = f"\\draw [color=red] ({x_real:.1f}, {y_real:.1f}) -- ({longitud:.1f}, {altura:.1f});"
            texto_cota = f"\\node [rotate = {angulo_grados}] at ({ubi_texto_x:.1f}, {ubi_texto_y:.1f}) {{{longitud_real:.2f}}};"
            if longitud_real > 8:
                texto = f"\\node [rotate = {angulo_grados}] at ({ubi_texto_x:.1f}, {ubi_texto_y-.5:.1f}) {{{tipo_caneria}}};"
            else:
                if longitud_real > 1.5:
                    texto = f"\\node [rotate = {angulo_grados}] at ({ubi_texto_x:.1f}, {ubi_texto_y-.5:.1f}) {{{tipo_caneria_abreviado}}};"
                else:
                    texto = f""
            return longitud, altura, linea,texto_cota,texto

def sube_o_baja(x_real, y_real, distancia):
    linea = f"\\draw [color=red] ({x_real:.1f}, {y_real:.1f}) -- ({x_real:.1f}, {y_real + distancia * 2.5:.1f});"
    texto_cota = f"\\node [rotate = 90] at ({x_real-.2:.1f}, {y_real+distancia:.1f}) {{{distancia:.2f}}};"
    return x_real, y_real+distancia*2.5 , linea,texto_cota


def isometrica(vectores, tipo_caneria,tipo_caneria_abreviado):

    # Verificar si la lista de vectores tiene menos de 1 elemento
    if len(vectores) < 2:
        primer_vector = vectores[0]
        (pv_x2, pv_y2) = primer_vector[1]
        vectores.insert(0,((pv_x2, pv_y2),(pv_x2, pv_y2+0.10)))
    
    primer_vector = vectores[0]
    vector_actual = vectores[1]
    (pv_x2, pv_y2) = primer_vector[1]
    (va_x1, va_y1), (va_x2, va_y2) = vector_actual
    distancia = math.sqrt((va_x2 - va_x1)**2 + (va_y2 - va_y1)**2)
    if va_x1 == va_x2:
        if va_y1 < va_y2:
            punto_actual = (va_x2, va_y2)
            #numero = float(input("Ingresa cuanto baja del medidor: "))
        else:
            punto_actual = (va_x1, va_y1)
            #numero = float(input("Ingresa cuanto baja del medidor: "))

        # Usar f-string para insertar el valor de 'numero' en la cadena
        resultados = [
            "\\draw [color=red] (0, 0) -- (0, 0.2) -- (.5, .5) -- (.5, -2);",
            "\\node [rotate = 30] at (0.2, 0.5) {0.15};",
            f"\\node [rotate = 90] at (0.3, -1.0) {{{numero:.2f}}};"
        ]

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
            #numero = float(input("Ingresa cuanto baja del medidor: "))
            resultados = ["\\draw [color=red] (0, 0) -- (0, 0.2) -- (.5, -0.1) -- (.5, -2);"
                          "\\node [rotate = -30] at (0.4, 0.2) {0.15};" 
                          f"\\node [rotate = 90] at (0.3, -4.0) {{{numero:.2f}}};"
                          ]
            x_real, y_real = .5, -2
        else:
            # izquierda 
            #numero = float(input("Ingresa cuanto baja del medidor: "))
            resultados = ["\\draw [color=red] (0, 0) -- (0, 0.2) -- (-.5, .5) -- (-.5, -2);"
                          "\\node [rotate = -30] at (-0.1, 0.5) {0.15};"
                          f"\\node [rotate = 90] at (-0.7, -4.0) {{{numero}}};"
                          ]
            x_real, y_real = -.5, -2
    # Decidir el índice de inicio del bucle según la distancia
    if distancia > 0.5:
        inicio_bucle = 1
    else:
        inicio_bucle = 2
    grados_anterior = 1
    angulo = 0
    # siguiente vector
    for vector_siguiente in vectores[inicio_bucle:]:
        (vs_x1, vs_y1), (vs_x2, vs_y2) = vector_siguiente
        (pa_x, pa_y) = punto_actual
        longitud_real = abs(vs_y2 - vs_y1 if vs_x1 == vs_x2 else vs_x2 - vs_x1)*2.5
        if longitud_real == 0:
            artefacto, distancia = menu_principal()
            if distancia is not None:
                x_real, y_real, linea, texto_cota = sube_o_baja(x_real,y_real, distancia)
            if artefacto is not None:
                resultados = dibujar_artefacto(x_real,y_real,artefacto, resultados)
                break
            grados_anterior = 90
        distancia = min(20, max(0.6, abs(vs_y2 - vs_y1 if vs_x1 == vs_x2 else vs_x2 - vs_x1)))
        if vs_x1 == vs_x2 and grados_anterior != 30 and longitud_real != 0:
            angulo = 30
            grados_anterior = angulo
            if ((vs_y1 + vs_y2) / 2) > pa_y:
                # izquierda
                x_real, y_real, linea,texto_cota,texto = dibujar_linea(x_real, y_real, distancia, angulo, -1, -1,longitud_real,tipo_caneria,tipo_caneria_abreviado)
            else:
                # derecha
                x_real, y_real, linea,texto_cota,texto = dibujar_linea(x_real, y_real, distancia, angulo, 1, 1,longitud_real,tipo_caneria,tipo_caneria_abreviado)
                
        else:
            if grados_anterior != 150 and longitud_real != 0:
                angulo = 150
                grados_anterior = angulo
                if ((vs_x1 + vs_x2) / 2) > pa_x:
                    # izquierda
                    x_real, y_real, linea,texto_cota,texto = dibujar_linea(x_real, y_real, distancia, angulo, 1, -1,longitud_real,tipo_caneria,tipo_caneria_abreviado)
                else:
                    # derecha
                    x_real, y_real, linea,texto_cota,texto = dibujar_linea(x_real, y_real, distancia, angulo, -1, 1,longitud_real,tipo_caneria,tipo_caneria_abreviado)
        resultados.append(texto_cota)
        resultados.append(linea)
        resultados.append(texto)
        distancia_1 = math.sqrt((pa_x - vs_x1)**2 + (pa_y - vs_y1)**2)
        distancia_2 = math.sqrt((pa_x - vs_x2)**2 + (pa_y - vs_y2)**2)
        
        if distancia_1 > distancia_2:
            punto_actual = (vs_x1, vs_y1)
        else:
            punto_actual = (vs_x2, vs_y2)
    
    return resultados

def dibujar_artefacto(x_real, y_real, artefacto, resultados):
    
    if ['1', '1', '2', '2'] == artefacto:
        texto = f'\\node[anchor=center] (nodo1) at ({x_real - 1.28:.1f}, {y_real + 0.18:.1f}){{\\begin{{tikzpicture}}[scale=1]\\input{{1.1.2.2}}L\\end{{tikzpicture}}}};'
        resultados.append(texto)
    if ['2', '1', '2', '2'] == artefacto:
        texto = f'\\node[anchor=center] (nodo1) at ({x_real +0.46:.1f}, {y_real + 0.6:.1f}){{\\begin{{tikzpicture}}[scale=1]\\input{{2.1.2.2}}L\\end{{tikzpicture}}}};'
        resultados.append(texto)

    if ['1', '1', '3', '1'] == artefacto:
        texto = f'\\node[anchor=center] (nodo1) at ({x_real -2.7:.1f}, {y_real + 0.90:.1f}){{\\begin{{tikzpicture}}[scale=1]\\input{{1.1.3.1}}L\\end{{tikzpicture}}}};'
        resultados.append(texto)

    if ['2', '1', '4', '1'] == artefacto:
        texto = f'\\node[anchor=center] (nodo1) at ({x_real -6.10 :.1f}, {y_real - 2.30:.1f}){{\\begin{{tikzpicture}}[scale=1]\\input{{2.1.4.1}}L\\end{{tikzpicture}}}};'
        resultados.append(texto)

    if ['2', '1', '3', '2'] == artefacto:
        texto = f'\\node[anchor=center] (nodo1) at ({x_real -6.10:.1f}, {y_real -2.3:.1f}){{\\begin{{tikzpicture}}[scale=1]\\input{{2.1.3.2}}L\\end{{tikzpicture}}}};'
        resultados.append(texto)

    return resultados

    
def troncal_caneria(ruta_entrada, ruta_salida,tipo_caneria,tipo_caneria_abreviado):
    vectores = leer_vectores(ruta_entrada)
    resultados = isometrica(vectores, tipo_caneria,tipo_caneria_abreviado)
    # Asignar puntos a los vectores más cercanos
    with open(ruta_salida, 'w') as archivo:
        for linea in resultados:
            archivo.write(linea + '\n')

numero = 0.65
# Ruta de los archivos
ruta_entrada = "/home/meli/planeargas/backend/src/txt_resultantes/caneria_optimizada.txt"
ruta_salida = "/home/meli/planeargas/backend/src/txt_resultantes/troncal_latex.txt"
tipo_caneria = "TUBO ACERO REVESTIDO POLIETILENO"
tipo_caneria_abreviado = "T.A.R.P."
# Ejecutar el proceso de optimización con proyección
troncal_caneria(ruta_entrada, ruta_salida,tipo_caneria, tipo_caneria_abreviado)
