# Databricks, DBT, and Airflow Project

## Overview

This project integrates Databricks, DBT, and Airflow to enable modern, scalable data engineering workflows.  
Below you'll find instructions for setting up Airflow 3.1.0 and integrating it with your pipeline.

---

## Airflow 3.1.0 Setup

### Prerequisites

- Python 3.8 or higher
- pip

### Setting up virtual environment and installing requirements

```sh 
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt 
```

### Installation of Airflow

Install Airflow 3.1.0 using pip and the official constraints file:

```sh
pip install apache-airflow==3.1.0 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.1.0/constraints-3.1.0.txt"
```

### Initialise Airflow 

1. Set AIRFLOW_HOME to your pwd 

```sh 
export AIRFLOW_HOME=~/airflow
```

2. Initialise Airflow database 

```sh 
airflow db init
```

3. Start Airflow services 

```sh 
airflow api-server -port 8080 

airflow scheduler 
```

4. Make sure dags are in the $AIRFLOW_HOME/dags folder 

5. Access Airflow UI using ```http://localhost:8080```

6. Stopping airflow services 

---

## Stopping Airflow Services

To stop Airflow webserver and scheduler:

```sh
pkill -f "airflow api-server"
pkill -f "airflow scheduler"
```

## Airflow User Setup

To create an admin user (if not already present):

```sh
airflow users create \
    --username admin \
    --firstname First \
    --lastname Last \
    --role Admin \
    --email admin@example.com \
    --password admin
```

### Troubleshooting

- **DAG not showing up:**  
  - Ensure your DAG file is in the `$AIRFLOW_HOME/dags` directory.
  - The file must end with `.py` and contain a valid `DAG` object.
  - Restart the scheduler and webserver after adding new DAGs.
  - Check logs in `$AIRFLOW_HOME/logs` for errors.

- **Port conflicts:**  
  - If port 8080 is in use, start the webserver on a different port:  
    ```sh
    airflow webserver --port 8081
    ```

- **Database backend:**  
  - For production, use PostgreSQL or MySQL instead of the default SQLite.  
    Update the `sql_alchemy_conn` setting in `airflow.cfg`.

### Environment Variables & Secrets

- Store sensitive credentials (API keys, database passwords) in Airflow Connections or environment variables.
- You can use a `.env` file and load it before starting Airflow:
  ```sh
  export $(cat .env | xargs)


---

### Databricks and dbt integration

For Databricks, configure your Airflow connection via the UI or CLI:

```sh
airflow connections add 'databricks_default' \
  --conn-type 'databricks' \
  --conn-host 'https://<your-databricks-instance>' \
    --conn-login '<token>' \
  --conn-password '<your-databricks-token>'

```

### Other useful airflow commands 

```sh

airflow dags list

airflow dags trigger <dag_id>

airflow tasks logs <dag_id> <task_id> <execution_date> 

airflow dags pause <dag_id>
airflow dags unpause <dag_id>

```