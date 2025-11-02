from datetime import datetime

from airflow.sdk import dag, task

from include.controllers.controller import get_bitcoin, save_bitcoin_into_db


@dag(
    dag_id='pegar_bitcoin',
    description='pipeline_para_capturar_preco_bitcoin',
    start_date=datetime(2025, 10, 23),
    schedule='*/15 * * * *',
    catchup=False
)
def pipeline():

    @task(task_id='pegar_preco_bitcoin')
    def task_get_bitcoin():
        return get_bitcoin()

    @task(task_id='salvar_bitcoin_no_banco_de_dados')
    def task_save_bitcoin_into_db(data):
        return save_bitcoin_into_db(data)

    t1 = task_get_bitcoin()
    t2 = task_save_bitcoin_into_db(t1)

    t1 >> t2

pipeline()