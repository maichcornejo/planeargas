import rasterio
import matplotlib.pyplot as plt
import numpy as np 

# Cargar el archivo GeoTIFF
with rasterio.open('/home/Maia/planeargas/backend/app/imagen_raster/caneria.tif') as dataset:
#with rasterio.open('red_areas_detected.tif') as dataset:
    # Leer la primera banda (en caso de imágenes en escala de grises o monocanal)
    band1 = dataset.read(1)

    # Si la imagen tiene más de un canal (RGB), puedes leer y combinar las bandas
    if dataset.count == 3:
        # Leer las tres bandas (Rojo, Verde, Azul)
        red = dataset.read(1)
        green = dataset.read(2)
        blue = dataset.read(3)

        # Combinar las bandas en una sola imagen
        rgb = np.dstack((red, green, blue))

        # Mostrar la imagen RGB
        plt.imshow(rgb)
    else:
        # Mostrar la imagen en escala de grises
        plt.imshow(band1, cmap='gray')

    plt.title('Imagen GeoTIFF')  # Cierra la cadena de texto correctamente
    plt.axis('on')  # no Ocultar los ejes para mejor visualización
    plt.show()