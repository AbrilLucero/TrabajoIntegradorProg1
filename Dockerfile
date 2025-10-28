# Imagen Python 3
FROM python:3.12-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos del proyecto dentro del contenedor
COPY . .

# Comando que se ejecutará al iniciar el contenedor
CMD ["python", "gestion_paises.py"]
