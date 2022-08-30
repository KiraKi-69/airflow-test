from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "open_pipline-0830214655",
}

dag = DAG(
    "open_pipline-0830214655",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.11.0 pipeline editor using `open_pipline.pipeline`.
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
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'open_pipline' --cos-endpoint http://elyra-minio.default.svc.cluster.local:9000 --cos-bucket elyra --cos-directory 'open_pipline-0830214655' --cos-dependencies-archive 'union_of_all_incoming_db-3fd2cb5b-2b04-45d3-91a9-d8bf04e65780.tar.gz' --file 'open_pipline/union_of_all_incoming_db.py' "
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

op_3fd2cb5b_2b04_45d3_91a9_d8bf04e65780.doc = """
        SQL-cбор сигналов из внешних и внутренних
    """


# Operator source: open_pipline/precalculating_signals.py


op_47de744d_6f27_48ef_af03_92f162c25205 = KubernetesPodOperator(
    name="Precalculate_all_signals",
    namespace="airflow",
    image="kiraki69/my-runtime-image:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'open_pipline' --cos-endpoint http://elyra-minio.default.svc.cluster.local:9000 --cos-bucket elyra --cos-directory 'open_pipline-0830214655' --cos-dependencies-archive 'precalculating_signals-47de744d-6f27-48ef-af03-92f162c25205.tar.gz' --file 'open_pipline/precalculating_signals.py' "
    ],
    task_id="Precalculate_all_signals",
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

op_47de744d_6f27_48ef_af03_92f162c25205.doc = """
        Предварительный расчет параметров факторов
    """

op_47de744d_6f27_48ef_af03_92f162c25205 << op_3fd2cb5b_2b04_45d3_91a9_d8bf04e65780


# Operator source: open_pipline/aggregate_signals.py


op_3809f722_780d_4237_bc15_1281a700ddaf = KubernetesPodOperator(
    name="Aggregate_precalc_signals",
    namespace="airflow",
    image="kiraki69/my-runtime-image:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'open_pipline' --cos-endpoint http://elyra-minio.default.svc.cluster.local:9000 --cos-bucket elyra --cos-directory 'open_pipline-0830214655' --cos-dependencies-archive 'aggregate_signals-3809f722-780d-4237-bc15-1281a700ddaf.tar.gz' --file 'open_pipline/aggregate_signals.py' "
    ],
    task_id="Aggregate_precalc_signals",
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

op_3809f722_780d_4237_bc15_1281a700ddaf.doc = """
        SQL-расчет агрегатов накопленных сигналов
    """

op_3809f722_780d_4237_bc15_1281a700ddaf << op_47de744d_6f27_48ef_af03_92f162c25205


# Operator source: open_pipline/calculating_signals.py


op_4358f515_88a8_4d67_a089_570d99468b59 = KubernetesPodOperator(
    name="Calculate_signals",
    namespace="airflow",
    image="kiraki69/my-runtime-image:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'open_pipline' --cos-endpoint http://elyra-minio.default.svc.cluster.local:9000 --cos-bucket elyra --cos-directory 'open_pipline-0830214655' --cos-dependencies-archive 'calculating_signals-4358f515-88a8-4d67-a089-570d99468b59.tar.gz' --file 'open_pipline/calculating_signals.py' "
    ],
    task_id="Calculate_signals",
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

op_4358f515_88a8_4d67_a089_570d99468b59.doc = """
        Окончательный расчет показателей сигналов
    """

op_4358f515_88a8_4d67_a089_570d99468b59 << op_3809f722_780d_4237_bc15_1281a700ddaf
