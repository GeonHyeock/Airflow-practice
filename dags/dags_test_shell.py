from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_test_shell",
    schedule="10 0 * * 6#1",
    start_date=pendulum.datetime(2024, 6, 25, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    t1_pizza = BashOperator(task_id="t1_pizza", bash_command="opt/airflow/plugins/shell/test.sh 피자")
    t2_hamburger = BashOperator(task_id="t2_hamburger", bash_command="opt/airflow/plugins/shell/test.sh 햄버거")

    t1_pizza >> t2_hamburger
