# Usamos una imagen base oficial de Python
FROM python:3.9-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el contenido de nuestro proyecto en el contenedor
COPY . .

# Instalamos las dependencias necesarias
RUN pip install Flask

# Exponemos el puerto en el que correrá la app (5000)
EXPOSE 5000

# Comando para ejecutar la app cuando el contenedor se inicie
CMD ["python", "app.py"]
