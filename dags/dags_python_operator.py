import pendulum
import datetime
import random
from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG(
    dag_id="dags_python_operator",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
) as dag:

    def select_food():
        food = ["햄버거", "피자", "치킨"]
        idx = random.randint(0, 2)
        print(food[idx])

    py_t1 = PythonOperator(
        task_id="py_t1",
        python_callable=select_food,
        ## 변수 할당 인자
        ## op_args
        ## op_kwargs
    )

    py_t1
