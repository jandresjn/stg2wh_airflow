from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

with DAG(
    dag_id='example_mysql_dag_single_connection',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:
    # Crear una nueva base de datos directamente en MySQL
    create_database = MySqlOperator(
        task_id='create_database',
        mysql_conn_id='mysql_root',
        sql="CREATE DATABASE IF NOT EXISTS example_db;"
    )

    # Crear una tabla dentro de la nueva base de datos
    create_table = MySqlOperator(
        task_id='create_table',
        mysql_conn_id='mysql_root',
        sql="""
        USE example_db;
        CREATE TABLE IF NOT EXISTS example_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
        """
    )

    # Insertar datos en la tabla recién creada
    insert_data = MySqlOperator(
        task_id='insert_data',
        mysql_conn_id='mysql_root',
        sql="""
        USE example_db;
        INSERT INTO example_table (name) VALUES ('Airflow');
        """
    )

    create_database >> create_table >> insert_data
