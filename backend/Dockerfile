# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos y luego instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto en el que tu aplicación se ejecutará
EXPOSE 8080

# Define el comando de inicio
<<<<<<< HEAD
CMD ["python", "app.py"]
=======
CMD ["python", "app.py"]
>>>>>>> 366618d8 (primer actualizacion melli)
