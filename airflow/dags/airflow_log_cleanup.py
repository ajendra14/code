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
    'start_date':  airflow.utils.dates.days_ago(2),
    'email': ['admin.accelerator@bizacuity.com'],
    'email_on_failure': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=30)
}

dag = DAG(
    'airflow_log_cleanup',
    schedule_interval='@weekly',
    dagrun_timeout=timedelta(minutes=60),
    default_args=default_args,
    max_active_runs=1,
    catchup=False
)

task = BashOperator(
    task_id='log_cleanup',
    bash_command='find ${AIRFLOW_HOME}/logs/ -type f -mtime +7 -delete ',
    dag=dag,
)

task
