from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

with DAG(
    dag_id='example_mysql_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:
    create_table = MySqlOperator(
        task_id='create_table',
        mysql_conn_id='mysql_default2',
        sql="""
        CREATE TABLE IF NOT EXISTS example_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
        """
    )

    insert_data = MySqlOperator(
        task_id='insert_data',
        mysql_conn_id='mysql_default2',
        sql="INSERT INTO example_table (name) VALUES ('Airflow');"
    )

    create_table >> insert_data
