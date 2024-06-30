from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime.now(),
}

dag = DAG(
    'example_php_dag5',
    default_args=default_args,
    schedule_interval='0 0 * * *',
    tags=['example'],
)

run_php_script = BashOperator(
    task_id='run_php_script',
    bash_command='php /opt/airflow/dags/schd_1/example_schd1.php',
    dag=dag,
)

run_php_script