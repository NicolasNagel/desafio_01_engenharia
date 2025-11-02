# 🚀 Desafio 01 - Engenharia de Dados

Este projeto implementa um **pipeline de dados automatizado** utilizando **Apache Airflow**, **Python**, **SQLAlchemy** e **Render (PostgreSQL hospedado)**.  
O objetivo é realizar a **extração, validação, transformação e carga** de dados de cotação do **Bitcoin (BTC)** em relação ao **Dólar (USD)**, salvando-os em um banco de dados relacional.

---

## 📂 Estrutura do Projeto

DESAFIO_01_ENGENHARIA/
├── dags/
│ ├── pipeline.py # DAG principal do Airflow
│ └── .airflowignore
│
├── include/
│ ├── controllers/
│ │ ├── controller.py # Camada de controle (extração e orquestração)
│ │ └── init.py
│ │
│ ├── database/
│ │ ├── db.py # Configuração da conexão com PostgreSQL
│ │ ├── db_models.py # Modelos ORM com SQLAlchemy
│ │ └── init.py
│ │
│ └── schemas/
│ ├── schema.py # Validação de dados com Pydantic
│ └── init.py
│
├── plugins/ # Plugins customizados (caso necessários)
│
├── tests/
│ └── dags/
│ └── test_dag_example.py # Teste básico de execução da DAG
│
├── Dockerfile # Configuração do ambiente Docker
├── airflow_settings.yaml # Definições de conexões e variáveis do Airflow
├── .env # Variáveis de ambiente (credenciais e configs)
├── .gitignore # Arquivos ignorados pelo Git
├── .dockerignore
└── .python-version # Versão utilizada no ambiente virtual


---

## 🧠 Fluxo do Pipeline

1. **Extração (Extract)**  
   A DAG coleta dados da cotação do Bitcoin através de uma API pública.  
   Exemplo de endpoint:  
   ```bash
   https://api.coinbase.com/v2/prices/BTC-USD/spot
2. **Validação (Validate)**
    Os dados recebidos são validados por modelos Pydantic definidos em schemas/schema.py, garantindo tipos corretos e presença de campos obrigatórios.
3. **Transformação (Transform)**
    Ajustes são aplicados aos campos de data, valores e formatação numérica antes da carga.
4. **Carga (Load)**
    Os dados validados são salvos no banco de dados PostgreSQL hospedado no Render.
    O SQLAlchemy gerencia a persistência através do modelo BitcoinTable.

## Modelo do Banco de Dados ##

Tabela: bitcoin

Campo	Tipo	Descrição
id	SERIAL PK	Identificador único
amount	NUMERIC	Valor da cotação
base	VARCHAR	Moeda base (BTC)
currency	VARCHAR	Moeda de conversão (USD)
timestamp	TIMESTAMP	Momento da coleta

Exemplo de dados:

id	amount	base	currency	timestamp
1	110.207,985	BTC	USD	2025-10-24 00:30:12.964
2	110.420,415	BTC	USD	2025-10-24 00:45:12.702
3	110.458,235	BTC	USD	2025-10-24 01

## Configuração do Ambiente ##
1. Clone o repositório
git clone https://github.com/seu-usuario/DESAFIO_01_ENGENHARIA.git
cd DESAFIO_01_ENGENHARIA

2. Crie o ambiente virtual
python -m venv .venv
source .venv/Scripts/activate   # Windows
# ou
source .venv/bin/activate       # Linux/Mac

3. Instale as dependências
pip install -r requirements.txt

4. Configure as variáveis de ambiente (.env)
DATABASE_URL=postgresql+psycopg2://usuario:senha@host:porta/nome_banco
API_URL=https://api.coinbase.com/v2/prices/BTC-USD/spot

5. Suba o ambiente do Airflow
astro dev start


Acesse o painel:
http://localhost:8080

Usuário padrão: admin | Senha: admin

## Deploy no Render ##

O banco PostgreSQL é hospedado no Render
.
Durante a execução, o pipeline envia as inserções diretamente para a instância configurada.

## Autor ##
Nicolas Nagel
Contato: [nicolascnagel@gmail.com]
Foco: Engenharia de Dados | Automação de Pipelines | Integração de APIs# desafio_01_engenharia
