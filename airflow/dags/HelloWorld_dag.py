# import os
from datetime import datetime
from airflow.models import DAG
from airflow.operators.bash import BashOperator

# from airflow.operators.python import PythonOperator
# from airflow.models import Variable


with DAG(
    dag_id="first_airflow_dag",
    schedule_interval="* * * * *",
    start_date=datetime(year=2022, month=2, day=1),
    catchup=False,
) as dag:

    # 1. Get current datetime
    task_get_datetime = BashOperator(
        task_id="get_datetime", bash_command="date"
    )
