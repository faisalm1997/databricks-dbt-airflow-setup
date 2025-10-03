# Databricks, DBT, and Airflow Project

## Overview

This project integrates Databricks, DBT, and Airflow to enable modern, scalable data engineering workflows.  
Below you'll find instructions for setting up Airflow 3.1.0 and integrating it with your pipeline.

---

## Airflow 3.1.0 Setup

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

Install Airflow 3.1.0 using pip and the official constraints file:

```sh
pip install apache-airflow==3.1.0 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.1.0/constraints-3.1.0.txt"

