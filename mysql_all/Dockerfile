FROM mysql:8.0
WORKDIR /mysql/data
ENV MYSQL_ROOT_PASSWORD=root
COPY data_warehouse_netflix.sql /docker-entrypoint-initdb.d/
COPY db_movies_neflix_transact.sql /docker-entrypoint-initdb.d/
