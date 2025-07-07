# Usamos imagen de Python3.10-slim para menos espacio usado
FROM python:3.10-slim

# Seleccionamos entorno de trabajo
WORKDIR /app

# Copiamos el archivo de requirements.txt
COPY requirements.txt .

# Instalamos las dependencias de Python sin caché desde el archivo de requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código de la aplicación directamente
COPY src/ ./src/
COPY tests/ ./tests/

# Corremos automáticamente las pruebas al iniciar
CMD ["pytest"]
