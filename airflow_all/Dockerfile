FROM apache/airflow:2.7.0

# Cambiar a usuario root para instalar dependencias del sistema
USER root

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    libmariadb-dev \
    && apt-get clean

# Cambiar al usuario 'airflow' antes de instalar paquetes de Python
USER airflow

# Instalar paquetes adicionales de Python
RUN pip install --no-cache-dir \
    mysql-connector-python \
    pandas

# Configurar el entorno de trabajo
WORKDIR /opt/airflow
