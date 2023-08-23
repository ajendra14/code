import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
import time
from airflow.models import Variable
import json

default_args = {
    'owner': 'airflow_admin',
    'start_date': datetime(2022, 7, 20),
    'email': ['admin.accelerator@bizacuity.com'],
    'email_on_failure': True,
    'retries': 3,
    'retry_delay': timedelta(minutes=10)
}

dag = DAG(
    'thg',
    schedule_interval='0 14-23/5 * * *',
    dagrun_timeout=timedelta(minutes=60),
    default_args=default_args,
    max_active_runs=1,
    catchup=False
)

task = BashOperator(
    task_id = 'thg_process',
    bash_command = 'sudo sh /home/accelerator/Accelerator/automated_shell_scripts/tomhorn_airflow.sh ',
    dag = dag,
)

task
