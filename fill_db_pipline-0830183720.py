from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "fill_db_pipline-0830183720",
}

dag = DAG(
    "fill_db_pipline-0830183720",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.11.0 pipeline editor using `fill_db_pipline.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: test_pipline/fill_db.py


op_9d669d87_db73_4704_b462_b2181fb94971 = KubernetesPodOperator(
    name="FillDB",
    namespace="airflow",
    image="continuumio/anaconda3:2021.11",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'fill_db_pipline' --cos-endpoint http://elyra-minio.default.svc.cluster.local:9000 --cos-bucket elyra --cos-directory 'fill_db_pipline-0830183720' --cos-dependencies-archive 'fill_db-9d669d87-db73-4704-b462-b2181fb94971.tar.gz' --file 'test_pipline/fill_db.py' "
    ],
    task_id="FillDB",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "YY8jIh2E00lSN37pEbje",
        "AWS_SECRET_ACCESS_KEY": "1LlixI7kW1QOEyQMDS8dzQWyDLCuAUE2a0PMQ2X0",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "fill_db_pipline-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)
