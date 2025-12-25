FROM apache/airflow:3.1.5-python3.13

USER root

RUN apt-get update && apt-get install -y vim curl

WORKDIR /opt/airflow

USER airflow

ENTRYPOINT ["airflow"]
