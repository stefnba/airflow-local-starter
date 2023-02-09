# airflow-local-starter

# Get Started

## Install Airflow

Setup virtual env with conda and activate it with the command that conda displays in the terminal.

```bash
conda create -p .conda python=3.10
```

The lastest currently avaialble Airflow version is 2.5.1.

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

## Setup Airflow

Now you have two option to finish the setup. The fast-track way is the standalone approach that will initialize the database, make a user, and start all components.

```bash
airflow standalone
```

The manual approach is the following.

```bash
airflow db init

airflow users create \
    --username admin \
    --firstname FirstName \
    --lastname LastName \
    --role Admin \
    --email user@mail.org

airflow scheduler -D
```

Then start the websever and scheduler in detached mode

```bash
airflow webserver
```

Now you can visit

```
http://localhost:8080
```

## Remove DAG examples

To come...
