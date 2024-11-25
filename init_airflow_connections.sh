#!/bin/bash
set -e

# Esperar a que el webserver esté disponible
echo "Esperando a que el Airflow Webserver esté listo..."
until curl -s http://airflow_webserver:8080 > /dev/null; do
  sleep 5
done

echo "Creando conexión 'mysql_root' en Airflow..."
airflow connections add 'mysql_root' \
    --conn-type 'mysql' \
    --conn-login 'airflow' \
    --conn-password 'airflow' \
    --conn-host 'mysql' \
    --conn-port '3306'

echo "Conexión 'mysql_root' creada exitosamente."
