import psycopg2
import cv2
import numpy as np

class identificar_artefactos:
    def __init__(self, db_params):
        # db_params es un diccionario con los parámetros de conexión a la base de datos
        self.db_params = db_params

    # Función para obtener las orientaciones e imágenes del artefacto desde la base de datos
    def obtener_orientaciones_artefacto(self, nombre_artefacto):
        conn = psycopg2.connect(**self.db_params)
        cur = conn.cursor()
        query = """
            SELECT orientacion, imagen 
            FROM artefactos 
            WHERE nombre = %s;
        """
        cur.execute(query, (nombre_artefacto,))
        orientaciones = cur.fetchall()
        conn.close()
        return orientaciones

    # Función para detectar artefactos comparando imágenes
    def detectar_artefacto(self, img_plano, nombre_artefacto):
        orientaciones = self.obtener_orientaciones_artefacto(nombre_artefacto)
        mejor_match = None
        mejor_orientacion = None
        mejor_punto = None

        for orientacion, imagen_binaria in orientaciones:
            nparr = np.frombuffer(imagen_binaria, np.uint8)
            img_artefacto = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            gray_plano = cv2.cvtColor(img_plano, cv2.COLOR_BGR2GRAY)
            gray_artefacto = cv2.cvtColor(img_artefacto, cv2.COLOR_BGR2GRAY)
            orb = cv2.ORB_create()
            kp1, des1 = orb.detectAndCompute(gray_plano, None)
            kp2, des2 = orb.detectAndCompute(gray_artefacto, None)
            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
            matches = bf.match(des1, des2)
            matches = sorted(matches, key=lambda x: x.distance)

            if matches and (mejor_match is None or len(matches) > len(mejor_match)):
                mejor_match = matches
                mejor_orientacion = orientacion
                mejor_punto = kp1[matches[0].queryIdx].pt

        if mejor_match:
            x, y = int(mejor_punto[0]), int(mejor_punto[1])
            with open('deteccion_artefactos.txt', 'a') as f:
                f.write(f"Artefacto: {nombre_artefacto}, Coordenadas: ({x}, {y}), Orientación: {mejor_orientacion}\n")
            print(f"Artefacto: {nombre_artefacto}, Coordenadas: ({x}, {y}), Orientación: {mejor_orientacion}")
        else:
            print(f"No se encontró {nombre_artefacto} en el plano.")

    # Función para procesar todos los artefactos en una imagen
    def procesar_artefactos(self, img_plano, artefactos):
        for nombre_artefacto in artefactos:
            self.detectar_artefacto(img_plano, nombre_artefacto)
