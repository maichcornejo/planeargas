import cv2
import numpy as np
from PIL import Image
import rasterio
from rasterio.transform import from_origin
from rasterio.crs import CRS
import pytesseract
import re
import os

# Paso 1: Convertir la imagen PNG a GeoTIFF de una sola banda
def convertir_png_a_geotiff(input_image_path, output_geotiff_path):
    # Cargar la imagen PNG
    image = Image.open(input_image_path)
    image_array = np.array(image)

    # Verificar si es RGB o RGBA, y si es necesario convertir a escala de grises
    if image_array.shape[2] == 4:
        image_array = image_array[:, :, :3]  # Eliminar el canal alfa si es necesario

    # Usar solo el canal rojo para crear la banda única
    band_red = image_array[:, :, 0]

    # Definir la transformación espacial
    transform = from_origin(west=0, north=0, xsize=1, ysize=1)
    crs = CRS.from_epsg(4326)  # Sistema de referencia espacial

    # Guardar como archivo GeoTIFF
    with rasterio.open(
            output_geotiff_path, 'w',
            driver='GTiff',
            height=band_red.shape[0],
            width=band_red.shape[1],
            count=1,
            dtype=band_red.dtype,
            crs=crs,
            transform=transform) as dst:
        dst.write(band_red, 1)

# Paso 2: Extraer el ancho del plano desde el texto en la imagen
def extraer_ancho_plano(image_path):
    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image)

    # Buscar el valor de ancho en el texto extraído (valor en el formato '15,65' o similar)
    width_match = re.search(r'\d{1,2}[,.]\d{1,2}', extracted_text)
    if width_match:
        plan_width = float(width_match.group().replace(",", "."))
        return plan_width
    else:
        raise ValueError("No se encontró el ancho del plano en el texto extraído.")

# Paso 3: Detección del medidor y cálculo de coordenadas
def detectar_medidor_y_calcular_coordenadas(input_geotiff_path, output_txt_path, output_latex_path, plan_width):
    # Cargar el archivo GeoTIFF
    with rasterio.open(input_geotiff_path) as dataset:
        image = dataset.read(1)  # Leer la primera banda

    # Convertir la imagen a escala de grises
    image_cv = np.array(image, dtype=np.uint8)
    blurred_image = cv2.GaussianBlur(image_cv, (5, 5), 0)

    # Detectar bordes
    edges = cv2.Canny(blurred_image, 50, 150)

    # Encontrar contornos
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Dimensiones esperadas del medidor en píxeles (ajustar según la escala)
    expected_width_range = (30, 50)
    expected_height_range = (20, 40)

    detected_meter = None
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if expected_width_range[0] <= w <= expected_width_range[1] and expected_height_range[0] <= h <= expected_height_range[1]:
            detected_meter = (x, y, w, h)
            break

    if detected_meter:
        x, y, w, h = detected_meter
        print(f"Medidor detectado en las coordenadas (x: {x}, y: {y}) con ancho {w} y altura {h}")
    else:
        raise ValueError("No se ha detectado el medidor en la imagen.")

    # Cálculo de coordenadas en metros basadas en el ancho del plano detectado
    image_width_pixels = image_cv.shape[1]
    image_height_pixels = image_cv.shape[0]

    # Escalas de conversión de píxeles a metros
    scale_x = plan_width / image_width_pixels
    scale_y = (plan_width * (image_height_pixels / image_width_pixels)) / image_height_pixels  # Escalado proporcional

    # **Corrección**: Cambiar el cálculo de y para que sea relativo a la esquina inferior izquierda
    meter_x_meters = x * scale_x
    meter_y_meters = (image_height_pixels - y - h) * scale_y  # Ajustar coordenadas Y para partir de abajo

    # Cálculo del centro del medidor en el eje X (considerando los lados izquierdo y derecho)
    meter_center_x_meters = meter_x_meters + (w * scale_x) / 2

    # Distancia desde el centro del medidor a los ejes medianeros
    distance_to_eje_medianero_izq = meter_center_x_meters  # Distancia desde el eje izquierdo
    distance_to_eje_medianero_der = plan_width - meter_center_x_meters  # Distancia desde el eje derecho

    # Paso 4: Generación del archivo TXT con las coordenadas y distancias
    with open(output_txt_path, 'w') as txt_file:
        txt_file.write(f"Coordenadas del Medidor (x, y): ({meter_x_meters:.2f}, {meter_y_meters:.2f}) metros\n")
        txt_file.write(f"Distancia al eje medianero izquierdo: {distance_to_eje_medianero_izq:.2f} metros\n")
        txt_file.write(f"Distancia al eje medianero derecho: {distance_to_eje_medianero_der:.2f} metros\n")

    # Paso 5: Generación del archivo LaTeX con las dimensiones del plano y ubicación del medidor
    tikz_coords = [
        (meter_x_meters, meter_y_meters),
        (meter_x_meters + w * scale_x, meter_y_meters),
        (meter_x_meters + w * scale_x, meter_y_meters + h * scale_y),
        (meter_x_meters, meter_y_meters + h * scale_y)
    ]
    
    with open(output_latex_path, 'w') as latex_file:
        # Escribir las dimensiones del plano
        latex_file.write(f"\\draw [help lines] (0, 0) grid ({plan_width}, {(plan_width * (image_height_pixels / image_width_pixels)):.2f});\n")
        
        # Dibujar el contorno del medidor
        for i in range(len(tikz_coords)):
            x1, y1 = tikz_coords[i]
            x2, y2 = tikz_coords[(i + 1) % len(tikz_coords)]  # Para cerrar el ciclo
            latex_file.write(f"\\draw [color=red] ({x1:.2f}, {y1:.2f}) -- ({x2:.2f}, {y2:.2f});\n")

    print(f"Archivo TXT generado en: {output_txt_path}")
    print(f"Archivo LaTeX generado en: {output_latex_path}")

# Rutas de archivo
input_image_path = '/home/Maia/planeargas/backend/src/imagen_entrada/planta_13.png'  # Archivo PNG subido
output_geotiff_path = '/home/Maia/planeargas/backend/src/imagen_salida/planta_geotiff.tif'
output_txt_path = '/home/Maia/planeargas/backend/src/txt_resultantes/medidor_coordenadas.txt'
output_latex_path = '/home/Maia/planeargas/backend/src/txt_resultantes/medidor1_coordenadas_tikz.tex'

# Extraer el ancho del plano automáticamente desde la imagen
plan_width = extraer_ancho_plano(input_image_path)
print(f"Ancho del plano extraído: {plan_width} metros")

# Ejecutar la conversión y análisis
convertir_png_a_geotiff(input_image_path, output_geotiff_path)
detectar_medidor_y_calcular_coordenadas(output_geotiff_path, output_txt_path, output_latex_path, plan_width)
