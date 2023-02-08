# airflow-local-starter


# Get Started

Setup virtual env with conda and activate it.
```bash
conda create -p .conda python=3.10
```

The lastest avaialble Airflow version is 2.5.1. 

To get the constraints file to setup Airflow, check that the following link works. If you want to install a different version or setup the environment with another version of Python, make sure the edit the version numbers `2.5.1` for Airflow and `3.10` for Python. 

```bash
https://raw.githubusercontent.com/apache/airflow/constraints-2.5.1/constraints-no-providers-3.10.txt
```

Once you've made sure the url works, run the following command to install Airflow.

```bash
pip install "apache-airflow==2.5.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.1/constraints-no-providers-3.10.txt"
```

Set the home directory of Airflow to the current project root directory. 

```bash
export AIRFLOW_HOME="$(pwd)/airflow"
```

Then run

```bash
airflow db init
airflow webserver -D
airflow scheduler -D
```

```bash
airflow users create \
          --username admin \
          --firstname FIRST_NAME \
          --lastname LAST_NAME \
          --role Admin \
          --email admin@example.org

```




