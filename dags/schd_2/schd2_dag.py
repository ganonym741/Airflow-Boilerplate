from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime.now(),
}

dag = DAG(
    'example_node_dag2',
    default_args=default_args,
    schedule_interval='@hourly',
    tags=['example'],
)

install_deps_schd2 = BashOperator(
    task_id='install_deps_schd2',
    bash_command='npm i',
    dag=dag,
    retries=3
)

build_node_schd2 = BashOperator(
    task_id='build_node_schd2',
    bash_command='npm run build',
    dag=dag,
)

run_node_schd2 = BashOperator(
    task_id='run_node_schd2',
    bash_command='npm run start',
    dag=dag,
)

install_deps_schd2 >> build_node_schd2 >> run_node_schd2

# wait_for_task = ExternalTaskSensor(
#     task_id='wait_for_task',
#     external_dag_id='other_dag',
#     external_task_id='other_task',
#     mode='poke',  # use 'reschedule' for better efficiency
#     timeout=600,  # timeout in seconds
#     dag=dag,
# )

# end = DummyOperator(
#     task_id='end',
#     dag=dag,
# )

# start >> wait_for_task >> end