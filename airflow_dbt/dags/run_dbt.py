from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

with DAG('dbt_databricks_pipeline',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    dbt_seed = BashOperator(
        task_id='dbt_seed',
        bash_command='dbt seed --profiles-dir /Users/faisalmomoniat/Documents/databricks-dbt-airflow/dbt_databricks'
    )

    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='dbt run --profiles-dir /Users/faisalmomoniat/Documents/databricks-dbt-airflow/dbt_databricks'
    )

    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='dbt test --profiles-dir /Users/faisalmomoniat/Documents/databricks-dbt-airflow/dbt_databricks'
    )

    dbt_seed >> dbt_run >> dbt_test