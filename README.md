# Apache Airflow

## Docker

Build custom image
```
docker build -t trungtvo/airflow:3.1.5-python3.13 .
```

Run Container:
```
docker run -it --name airflow-ctn \
    -h airflow-cluster \
    -p 8080:8080 \
    -e AIRFLOW__CORE__LOAD_EXAMPLES=False \
    -v ./dags:/opt/airflow/dags \
    trungtvo/airflow:3.1.5-python3.13 standalone
```

Access into container
```
docker exec -it airflow-ctn /bin/bash
```

Check `Airflow` config
```
airflow info
```

List all dags
```
airflow dags list
```

`Airflow` comes with many prebuilt sample DAGs. To understand more, copy a sample DAG to local `dags` folder to examine:
```
docker cp airflow-ctn:/home/airflow/.local/lib/python3.13/site-packages/airflow/example_dags/standard/example_bash_operator.py ./dags
```

## Manual Setup

Setup envs
```
export AIRFLOW_HOME=~/workspace/airflow
export AIRFLOW_VERSION=3.1.5
export PYTHON_VERSION="$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
```

Install `airflow`
```
pip3 install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```
