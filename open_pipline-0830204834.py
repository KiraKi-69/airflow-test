from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "open_pipline-0830204834",
}

dag = DAG(
    "open_pipline-0830204834",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.11.0 pipeline editor using `untitled.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: open_pipline/union_of_all_incoming_db.py


op_3fd2cb5b_2b04_45d3_91a9_d8bf04e65780 = KubernetesPodOperator(
    name="Union_of_all_tables",
    namespace="airflow",
    image="kiraki69/my-runtime-image:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'open_pipline' --cos-endpoint http://elyra-minio.default.svc.cluster.local:9000 --cos-bucket elyra --cos-directory 'open_pipline-0830204834' --cos-dependencies-archive 'union_of_all_incoming_db-3fd2cb5b-2b04-45d3-91a9-d8bf04e65780.tar.gz' --file 'open_pipline/union_of_all_incoming_db.py' "
    ],
    task_id="Union_of_all_tables",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "YY8jIh2E00lSN37pEbje",
        "AWS_SECRET_ACCESS_KEY": "1LlixI7kW1QOEyQMDS8dzQWyDLCuAUE2a0PMQ2X0",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "open_pipline-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)
