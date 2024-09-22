import rasterio
import numpy as np
import json
from scipy.ndimage import label, center_of_mass
from rasterio.transform import Affine

# Rutas de las imágenes raster
ARTEFACTOS_PATH = '/home/Maia/planeargas/backend/src/imagen_raster/artefactos.tif'
VENTILACIONES_PATH = '/home/Maia/planeargas/backend/src/imagen_raster/ventilaciones.tif'
OUTPUT_FILE_JSON = '/home/Maia/planeargas/backend/src/detecciones/detecciones.json'
OUTPUT_FILE_LATEX = '/home/Maia/planeargas/backend/src/detecciones/detecciones.tex'

# Factor de escala para reducir las coordenadas
FACTOR_ESCALA = 0.01

def cargar_imagen(path):
    """
    Carga una imagen raster y retorna los datos, la transformación y el CRS.
    """
    with rasterio.open(path) as src:
        data = src.read(1)  # Leer la primera banda
        transform = src.transform
        crs = src.crs
    return data, transform, crs

def obtener_valores_unicos(data):
    """
    Devuelve los valores únicos en la imagen raster para ayudar en la detección de objetos.
    """
    valores_unicos = np.unique(data)
    print("Valores únicos en la imagen:", valores_unicos)
    return valores_unicos

def agrupar_pixeles(data, valor_objeto):
    """
    Agrupa los píxeles contiguos que tienen el mismo valor de objeto.
    Retorna los centroides de los grupos de píxeles.
    """
    # Crear una máscara de píxeles que coincidan con el valor del objeto
    mask = data == valor_objeto

    # Etiquetar los píxeles contiguos
    labeled_array, num_features = label(mask)
    
    # Calcular los centroides de los grupos
    centroides = center_of_mass(mask, labeled_array, range(1, num_features + 1))
    
    return centroides

def transformar_coordenadas(centroides, transform):
    """
    Transforma los centroides de las áreas agrupadas a coordenadas geográficas.
    Aplica una escala para reducir el tamaño del dibujo.
    Retorna una lista de diccionarios con 'x' y 'y'.
    """
    coordenadas = []
    for centroide in centroides:
        fila, columna = centroide
        x, y = rasterio.transform.xy(transform, fila, columna, offset='center')
        # Aplicar el factor de escala
        x_escala = x * FACTOR_ESCALA
        y_escala = y * FACTOR_ESCALA
        coordenadas.append({'x': x_escala, 'y': y_escala})
    return coordenadas

def generar_archivo_intermedio(artefactos, ventilaciones, crs):
    """
    Genera un archivo JSON con las ubicaciones de artefactos y ventilaciones.
    """
    detecciones = {
        'crs': crs.to_string(),
        'artefactos': artefactos,
        'ventilaciones': ventilaciones
    }
    with open(OUTPUT_FILE_JSON, 'w') as f:
        json.dump(detecciones, f, indent=4)

def generar_archivo_latex(artefactos, ventilaciones):
    """
    Genera un archivo LaTeX utilizando TikZ para graficar las posiciones de artefactos y ventilaciones.
    """
    with open(OUTPUT_FILE_LATEX, 'w') as f:
        f.write("\\documentclass{article}\n")
        f.write("\\usepackage{tikz}\n")
        f.write("\\begin{document}\n")
        f.write("\\begin{tikzpicture}\n")

        # Graficar artefactos (en rojo)
        for artefacto in artefactos:
            f.write(f"\\fill[red] ({artefacto['x']},{artefacto['y']}) circle (2pt);\n")

        # Graficar ventilaciones (en verde)
        for ventilacion in ventilaciones:
            f.write(f"\\fill[green] ({ventilacion['x']},{ventilacion['y']}) circle (2pt);\n")

        f.write("\\end{tikzpicture}\n")
        f.write("\\end{document}\n")

def procesar_imagenes():
    """
    Orquesta el procesamiento de las imágenes raster para detectar artefactos y ventilaciones.
    """
    # Cargar imágenes
    data_artefactos, transform_artefactos, crs_artefactos = cargar_imagen(ARTEFACTOS_PATH)
    data_ventilaciones, transform_ventilaciones, crs_ventilaciones = cargar_imagen(VENTILACIONES_PATH)

    # Verificar los valores únicos en las imágenes
    print("Valores únicos en artefactos:")
    obtener_valores_unicos(data_artefactos)
    print("Valores únicos en ventilaciones:")
    obtener_valores_unicos(data_ventilaciones)

    # Verificar que ambas imágenes tengan la misma proyección
    if crs_artefactos != crs_ventilaciones:
        raise ValueError("Las imágenes raster no tienen la misma proyección.")

    # Definir los valores que representan artefactos y ventilaciones
    VALOR_ARTEFACTO = 128  # Este valor parece correcto
    VALOR_VENTILACION = 255  # Valor para ventilaciones detectado previamente

    # Agrupar píxeles de artefactos y ventilaciones
    centroides_artefactos = agrupar_pixeles(data_artefactos, VALOR_ARTEFACTO)
    centroides_ventilaciones = agrupar_pixeles(data_ventilaciones, VALOR_VENTILACION)

    # Transformar centroides a coordenadas geográficas con escala
    coordenadas_artefactos = transformar_coordenadas(centroides_artefactos, transform_artefactos)
    coordenadas_ventilaciones = transformar_coordenadas(centroides_ventilaciones, transform_ventilaciones)

    # Generar archivo intermedio JSON
    generar_archivo_intermedio(coordenadas_artefactos, coordenadas_ventilaciones, crs_artefactos)

    # Generar archivo LaTeX para visualizar las ubicaciones
    generar_archivo_latex(coordenadas_artefactos, coordenadas_ventilaciones)

    print(f"Detecciones guardadas en {OUTPUT_FILE_JSON} y {OUTPUT_FILE_LATEX}")

if __name__ == "__main__":
    procesar_imagenes()
