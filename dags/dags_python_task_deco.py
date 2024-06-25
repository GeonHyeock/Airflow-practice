import pendulum
import datetime
import random
from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator

with DAG(
    dag_id="dags_python_task_deco",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    @task(task_id="python_task_1")
    def print_context(my_input):
        print(my_input)

    python_task_1 = print_context("deco 실행")
