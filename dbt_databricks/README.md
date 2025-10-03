# dbt + Databricks Integration Project

This project demonstrates how to connect dbt and databricks for data transformation as part of the data engineering lifecycle.

---

## Prerequisites

- [Python 3.7+](https://www.python.org/downloads/)
- [dbt-databricks](https://docs.getdbt.com/reference/adapter/databricks) (`pip install dbt-databricks`)
- A Databricks workspace and SQL Warehouse
- A Databricks Personal Access Token

---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/faisalm1997/databricks-dbt-airflow
cd dbt_databricks
```

### 2. Install dbt-databricks

```sh
pip install dbt-core
pip install dbt-databricks
```

### 3. Configure Your dbt Profile

You can configure your Databricks connection in one of two ways:

#### **A. Using Environment Variables (Recommended for Security)**

Set the following environment variables in your terminal or `.env` file:

```sh
export DBT_HOST=<your-databricks-workspace-url>
export DBT_HTTP_PATH=<your-sql-warehouse-http-path>
export DBT_TOKEN=<your-databricks-personal-access-token>
export DBT_CATALOG=your_catalog_name   # or your catalog name
export DBT_SCHEMA=your_schema_name           # or your schema name
```

Your `profiles.yml` should look like:

```yaml
dbt_databricks:
  target: dev
  outputs:
    dev:
      type: databricks
      catalog: "{{ env_var('DBT_CATALOG', 'your_catalog_name') }}"
      schema: "{{ env_var('DBT_SCHEMA', 'your_schema_name') }}"
      host: "{{ env_var('DBT_HOST') }}"
      http_path: "{{ env_var('DBT_HTTP_PATH') }}"
      token: "{{ env_var('DBT_TOKEN') }}"
      threads: 1
```

#### **B. Using Hardcoded Values in `profiles.yml`**

Edit your `~/.dbt/profiles.yml` (or use `--profiles-dir` to point to a custom location):

```yaml
dbt_databricks:
  target: dev
  outputs:
    dev:
      type: databricks
      catalog: <your-catalog-name>
      schema: <your-schema-name>
      host: <your-databricks-workspace-url>
      http_path: <your-sql-warehouse-http-path>
      token: <your-databricks-personal-access-token>
      threads: 1
```

---

## Running dbt Commands

After configuring your profile, you can run dbt commands as usual:

```sh
dbt debug # To test the connection
dbt run # To run dbt models
dbt test # To run dbt tests configured for the models
dbt docs generate # To generate data lineage docs
dbt docs serve # To produce the data lineage docs for viewing
```

If your `profiles.yml` is not in the default location (`~/.dbt`), use:

```sh
dbt run --profiles-dir /path/to/your/profiles/dir
```

---

## Resources

- [dbt Databricks Adapter Docs](https://docs.getdbt.com/reference/adapter/databricks)
- [dbt Documentation](https://docs.getdbt.com/docs/introduction)

---

## Troubleshooting

- Ensure your Databricks SQL Warehouse is running.
- Double-check your token, host, and http_path values.
- Use `dbt debug` to verify your connection.

---

This quick setup guide should enable you to start developing models and transforming data in databricks using dbt.