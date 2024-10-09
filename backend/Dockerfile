# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requerimientos y instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto que usará la aplicación
EXPOSE 8080

# Comando por defecto (puede ser sobreescrito por docker-compose)
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]

ENV PYTHONPATH=/app
