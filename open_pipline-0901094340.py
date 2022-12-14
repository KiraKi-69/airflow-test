from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "open_pipline-0901094340",
}

dag = DAG(
    "open_pipline-0901094340",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.11.0 pipeline editor using `open_pipline.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: open_pipline/cb_signals.py


op_5191ae42_0210_443d_af90_b69148878fd7 = KubernetesPodOperator(
    name="CRE_signals_ingest",
    namespace="airflow",
    image="kiraki69/my-runtime-image:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'open_pipline' --cos-endpoint http://elyra-minio.default.svc.cluster.local:9000 --cos-bucket elyra --cos-directory 'open_pipline-0901094340' --cos-dependencies-archive 'cb_signals-5191ae42-0210-443d-af90-b69148878fd7.tar.gz' --file 'open_pipline/cb_signals.py' "
    ],
    task_id="CRE_signals_ingest",
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


# Operator source: open_pipline/dwh_signals.py


op_c68643b8_c317_4e13_a1ab_69b46d0f4806 = KubernetesPodOperator(
    name="DWH_signals_ingest",
    namespace="airflow",
    image="kiraki69/my-runtime-image:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'open_pipline' --cos-endpoint http://elyra-minio.default.svc.cluster.local:9000 --cos-bucket elyra --cos-directory 'open_pipline-0901094340' --cos-dependencies-archive 'dwh_signals-c68643b8-c317-4e13-a1ab-69b46d0f4806.tar.gz' --file 'open_pipline/dwh_signals.py' "
    ],
    task_id="DWH_signals_ingest",
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


# Operator source: open_pipline/spark_signals.py


op_ff67c6d4_5546_45fb_9e5b_bdb79eea0887 = KubernetesPodOperator(
    name="Attribute_signals_ingest",
    namespace="airflow",
    image="kiraki69/my-runtime-image:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'open_pipline' --cos-endpoint http://elyra-minio.default.svc.cluster.local:9000 --cos-bucket elyra --cos-directory 'open_pipline-0901094340' --cos-dependencies-archive 'spark_signals-ff67c6d4-5546-45fb-9e5b-bdb79eea0887.tar.gz' --file 'open_pipline/spark_signals.py' "
    ],
    task_id="Attribute_signals_ingest",
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


# Operator source: open_pipline/manual_signals.py


op_a159bc1d_8a94_42fe_a13f_d16cbb6c647d = KubernetesPodOperator(
    name="Manual_signals_ingest",
    namespace="airflow",
    image="kiraki69/my-runtime-image:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'open_pipline' --cos-endpoint http://elyra-minio.default.svc.cluster.local:9000 --cos-bucket elyra --cos-directory 'open_pipline-0901094340' --cos-dependencies-archive 'manual_signals-a159bc1d-8a94-42fe-a13f-d16cbb6c647d.tar.gz' --file 'open_pipline/manual_signals.py' "
    ],
    task_id="Manual_signals_ingest",
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


# Operator source: open_pipline/precalculating_signals.py


op_47de744d_6f27_48ef_af03_92f162c25205 = KubernetesPodOperator(
    name="Precalculate_factor_parameters",
    namespace="airflow",
    image="kiraki69/my-runtime-image:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'open_pipline' --cos-endpoint http://elyra-minio.default.svc.cluster.local:9000 --cos-bucket elyra --cos-directory 'open_pipline-0901094340' --cos-dependencies-archive 'precalculating_signals-47de744d-6f27-48ef-af03-92f162c25205.tar.gz' --file 'open_pipline/precalculating_signals.py' "
    ],
    task_id="Precalculate_factor_parameters",
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
        ?????????????????????????????? ???????????? ???????????????????? ????????????????
    """

op_47de744d_6f27_48ef_af03_92f162c25205 << op_5191ae42_0210_443d_af90_b69148878fd7

op_47de744d_6f27_48ef_af03_92f162c25205 << op_c68643b8_c317_4e13_a1ab_69b46d0f4806

op_47de744d_6f27_48ef_af03_92f162c25205 << op_ff67c6d4_5546_45fb_9e5b_bdb79eea0887

op_47de744d_6f27_48ef_af03_92f162c25205 << op_a159bc1d_8a94_42fe_a13f_d16cbb6c647d


# Operator source: open_pipline/aggregate_signals.py


op_3809f722_780d_4237_bc15_1281a700ddaf = KubernetesPodOperator(
    name="Aggregate_signals",
    namespace="airflow",
    image="kiraki69/my-runtime-image:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'open_pipline' --cos-endpoint http://elyra-minio.default.svc.cluster.local:9000 --cos-bucket elyra --cos-directory 'open_pipline-0901094340' --cos-dependencies-archive 'aggregate_signals-3809f722-780d-4237-bc15-1281a700ddaf.tar.gz' --file 'open_pipline/aggregate_signals.py' "
    ],
    task_id="Aggregate_signals",
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
        SQL-???????????? ?????????????????? ?????????????????????? ????????????????
    """

op_3809f722_780d_4237_bc15_1281a700ddaf << op_47de744d_6f27_48ef_af03_92f162c25205


# Operator source: open_pipline/calculating_signals.py


op_4358f515_88a8_4d67_a089_570d99468b59 = KubernetesPodOperator(
    name="Calculate_factors",
    namespace="airflow",
    image="kiraki69/my-runtime-image:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'open_pipline' --cos-endpoint http://elyra-minio.default.svc.cluster.local:9000 --cos-bucket elyra --cos-directory 'open_pipline-0901094340' --cos-dependencies-archive 'calculating_signals-4358f515-88a8-4d67-a089-570d99468b59.tar.gz' --file 'open_pipline/calculating_signals.py' "
    ],
    task_id="Calculate_factors",
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
        ?????????????????????????? ???????????? ?????????????????????? ????????????????
    """

op_4358f515_88a8_4d67_a089_570d99468b59 << op_3809f722_780d_4237_bc15_1281a700ddaf


# Operator source: open_pipline/move_greendata_responses_to_foctor_dm.py


op_26a44a77_a534_44ff_acf4_59f711c3dfa1 = KubernetesPodOperator(
    name="Approved_factors_ingest",
    namespace="airflow",
    image="kiraki69/my-runtime-image:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'open_pipline' --cos-endpoint http://elyra-minio.default.svc.cluster.local:9000 --cos-bucket elyra --cos-directory 'open_pipline-0901094340' --cos-dependencies-archive 'move_greendata_responses_to_foctor_dm-26a44a77-a534-44ff-acf4-59f711c3dfa1.tar.gz' --file 'open_pipline/move_greendata_responses_to_foctor_dm.py' "
    ],
    task_id="Approved_factors_ingest",
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


# Operator source: open_pipline/move_signals_to_factor.py


op_82bfd12d_9ea0_4edc_a603_5cde10e281a6 = KubernetesPodOperator(
    name="Feed_factors_DM",
    namespace="airflow",
    image="kiraki69/my-runtime-image:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'open_pipline' --cos-endpoint http://elyra-minio.default.svc.cluster.local:9000 --cos-bucket elyra --cos-directory 'open_pipline-0901094340' --cos-dependencies-archive 'move_signals_to_factor-82bfd12d-9ea0-4edc-a603-5cde10e281a6.tar.gz' --file 'open_pipline/move_signals_to_factor.py' "
    ],
    task_id="Feed_factors_DM",
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

op_82bfd12d_9ea0_4edc_a603_5cde10e281a6 << op_4358f515_88a8_4d67_a089_570d99468b59

op_82bfd12d_9ea0_4edc_a603_5cde10e281a6 << op_26a44a77_a534_44ff_acf4_59f711c3dfa1


# Operator source: open_pipline/factor_dm_to_recalc.py


op_b08c325f_0c42_4076_990c_032e7d9052f3 = KubernetesPodOperator(
    name="Feed_recalc_request_DM",
    namespace="airflow",
    image="kiraki69/my-runtime-image:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'open_pipline' --cos-endpoint http://elyra-minio.default.svc.cluster.local:9000 --cos-bucket elyra --cos-directory 'open_pipline-0901094340' --cos-dependencies-archive 'factor_dm_to_recalc-b08c325f-0c42-4076-990c-032e7d9052f3.tar.gz' --file 'open_pipline/factor_dm_to_recalc.py' "
    ],
    task_id="Feed_recalc_request_DM",
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

op_b08c325f_0c42_4076_990c_032e7d9052f3 << op_82bfd12d_9ea0_4edc_a603_5cde10e281a6


# Operator source: open_pipline/factor_dm_to_dpa.py


op_92763c26_00a7_4000_926f_c6d5e76805a0 = KubernetesPodOperator(
    name="Feed_DPA_DM",
    namespace="airflow",
    image="kiraki69/my-runtime-image:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'open_pipline' --cos-endpoint http://elyra-minio.default.svc.cluster.local:9000 --cos-bucket elyra --cos-directory 'open_pipline-0901094340' --cos-dependencies-archive 'factor_dm_to_dpa-92763c26-00a7-4000-926f-c6d5e76805a0.tar.gz' --file 'open_pipline/factor_dm_to_dpa.py' "
    ],
    task_id="Feed_DPA_DM",
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

op_92763c26_00a7_4000_926f_c6d5e76805a0 << op_82bfd12d_9ea0_4edc_a603_5cde10e281a6


# Operator source: open_pipline/move_signals_to_approvement.py


op_59624512_7592_4cbc_acaf_663810864748 = KubernetesPodOperator(
    name="Feed_manual_approving_DM",
    namespace="airflow",
    image="kiraki69/my-runtime-image:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'open_pipline' --cos-endpoint http://elyra-minio.default.svc.cluster.local:9000 --cos-bucket elyra --cos-directory 'open_pipline-0901094340' --cos-dependencies-archive 'move_signals_to_approvement-59624512-7592-4cbc-acaf-663810864748.tar.gz' --file 'open_pipline/move_signals_to_approvement.py' "
    ],
    task_id="Feed_manual_approving_DM",
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

op_59624512_7592_4cbc_acaf_663810864748 << op_4358f515_88a8_4d67_a089_570d99468b59
