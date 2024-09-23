import cv2
import numpy as np

def proceso_deteccion_llave_de_paso(ruta_imagen):
    # Cargar la imagen usando OpenCV

    imagen = cv2.imread(ruta_imagen)

    # Convertir la imagen a RGB (OpenCV la carga como BGR por defecto)
    imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

    # Definir los rangos de colores para gris (artefactos) y rojo (llaves de paso) en formato RGB
    gris_inferior_exacto = np.array([128, 128, 128])  # Gris exacto para los artefactos
    gris_superior_exacto = np.array([128, 128, 128])  # Gris exacto para los artefactos

    rojo_inferior = np.array([200, 0, 0])  # Límite inferior para las llaves rojas
    rojo_superior = np.array([255, 50, 50])  # Límite superior para las llaves rojas

    # Crear máscaras para aislar las áreas grises (artefactos) y rojas (llaves)
    mascara_gris_exacto = cv2.inRange(imagen_rgb, gris_inferior_exacto, gris_superior_exacto)
    mascara_roja = cv2.inRange(imagen_rgb, rojo_inferior, rojo_superior)

    # Encontrar contornos para los artefactos grises
    contornos_gris_exacto, _ = cv2.findContours(mascara_gris_exacto, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Encontrar contornos para las llaves rojas
    contornos_rojos, _ = cv2.findContours(mascara_roja, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Crear una imagen en blanco para dibujar los contornos de artefactos y llaves
    imagen_salida = np.zeros_like(imagen_rgb)

    # Dibujar los artefactos grises exactos en la imagen de salida
    cv2.drawContours(imagen_salida, contornos_gris_exacto, -1, (128, 128, 128), thickness=cv2.FILLED)

    # Dibujar las llaves rojas en la imagen de salida
    cv2.drawContours(imagen_salida, contornos_rojos, -1, (255, 0, 0), thickness=cv2.FILLED)

    # Guardar la imagen procesada
    ruta_imagen_salida = "/home/meli/planeargas/backend/src/detecciones/artefactos_y_llaves_exactos.png"

    # Analizar las posiciones de las llaves rojas en relación con los artefactos grises
    posiciones_artefacto_llave = []

    # Aumentar el umbral de alineación para detectar más casos (ej., de 50 a 100)
    umbral_alineacion = 100

    # Inicializar contador para los artefactos
    contador_artefactos = 1

    for contorno_gris in contornos_gris_exacto:
        # Obtener el centro del artefacto gris
        M_gris = cv2.moments(contorno_gris)
        if M_gris["m00"] != 0:
            cx_gris = int(M_gris["m10"] / M_gris["m00"])
            cy_gris = int(M_gris["m01"] / M_gris["m00"])

            # Obtener los límites del artefacto
            x, y, w, h = cv2.boundingRect(contorno_gris)

            # Verificar si el artefacto tiene una llave cercana
            llave_encontrada = False
            for contorno_rojo in contornos_rojos:
                # Obtener el centro de la llave roja
                M_rojo = cv2.moments(contorno_rojo)
                if M_rojo["m00"] != 0:
                    cx_rojo = int(M_rojo["m10"] / M_rojo["m00"])
                    cy_rojo = int(M_rojo["m01"] / M_rojo["m00"])

                    # Determinar si la llave está a la izquierda, derecha o debajo del artefacto
                    if abs(cy_gris - cy_rojo) < umbral_alineacion:  # Umbral para detectar horizontalmente
                        llave_encontrada = True
                        if cx_rojo < cx_gris:
                            posicion = "derecha"  # Invertido
                        else:
                            posicion = "izquierda"  # Invertido
                        posiciones_artefacto_llave.append((contador_artefactos, cx_gris, cy_gris, posicion))
                    # Verificar si la llave está directamente debajo del artefacto
                    elif cx_gris - (w / 2) <= cx_rojo <= cx_gris + (w / 2) and cy_rojo > cy_gris:
                        llave_encontrada = True
                        posicion = "debajo"
                        posiciones_artefacto_llave.append((contador_artefactos, cx_gris, cy_gris, posicion))

            # Si no se encontró una llave directamente, analizar la concentración de rojo alrededor del artefacto
            if not llave_encontrada:
                # Definir el área de interés (a la izquierda y derecha del artefacto)
                region_izquierda = mascara_roja[cy_gris - 50:cy_gris + 50, cx_gris - 100:cx_gris]
                region_derecha = mascara_roja[cy_gris - 50:cy_gris + 50, cx_gris:cx_gris + 100]

                # Sumar los píxeles rojos en cada región
                suma_izquierda = np.sum(region_izquierda)
                suma_derecha = np.sum(region_derecha)

                # Determinar qué lado tiene más píxeles rojos
                if suma_izquierda > suma_derecha:
                    posicion = "derecha"  # Invertido
                else:
                    posicion = "izquierda"  # Invertido

                # Agregar el resultado basado en la concentración de rojo
                posiciones_artefacto_llave.append((contador_artefactos, cx_gris, cy_gris, posicion))

            # Dibujar el número del artefacto en la imagen
            cv2.putText(imagen_salida, f"A{contador_artefactos}", (cx_gris, cy_gris), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            # Incrementar el contador para el siguiente artefacto
            contador_artefactos += 1

    # Guardar la imagen con los números de los artefactos
    cv2.imwrite(ruta_imagen_salida, cv2.cvtColor(imagen_salida, cv2.COLOR_RGB2BGR))

    # Guardar los resultados en un archivo de texto con los números de artefactos
    ruta_texto_salida = '/home/meli/planeargas/backend/src/detecciones/deteccion_llaves_exactas.txt'
    with open(ruta_texto_salida, 'w') as f:
        for posicion_artefacto in posiciones_artefacto_llave:
            f.write(f"Artefacto {posicion_artefacto[0]} en ({posicion_artefacto[1]}, {posicion_artefacto[2]}) tiene la llave a la {posicion_artefacto[3]}.\n")

    print(f"Imagen procesada guardada en {ruta_imagen_salida}")
    print(f"Resultados de detección guardados en {ruta_texto_salida}")