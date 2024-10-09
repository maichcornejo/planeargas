# Usa la versión 18 de Node.js como base
FROM node:18-alpine

# Establecer el directorio de trabajo
WORKDIR /home/node/cli

# Copiar solo package.json y package-lock.json
COPY package*.json ./

# Instalar las dependencias
RUN npm install 
# Instalar Angular CLI globalmente
RUN npm install -g @angular/cli

# Copiar los archivos de la aplicación
COPY . .

# Exponer el puerto
EXPOSE 4200

# Comando para iniciar la aplicación Angular
CMD ["ng", "serve", "--host", "0.0.0.0"]
