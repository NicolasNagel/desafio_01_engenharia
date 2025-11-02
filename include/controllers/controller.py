import requests

from include.schemas.schema import BitcoinSchema
from include.database.db import SessionLocal, engine, Base
from include.database.db_models import BitcoinTable

Base.metadata.create_all(bind=engine)

def get_bitcoin() -> BitcoinSchema | None:
    """
    Função que faz a requisição na URL da Coinbase 
    e retorna o dado validado pelo Pydantic.

    Argumentos:
        - None

    Retorno:
        - BitcoinSchema: Schema Bitcoin validado pelo Pydantic.
    """
    try:
        response = requests.get('https://api.coinbase.com/v2/prices/spot')
        if response.status_code == 200:
            resultado = response.json()
            data = resultado.get('data', {})
            
            return BitcoinSchema(**data)
        
        else:
            print("Sem retorno da API")
            return None

    except Exception as e:
        print("Sem retorno da API.")
        return None

def save_bitcoin_into_db(data: BitcoinSchema) -> BitcoinTable | None:
    """
    Recebe um schema do Pydantic e faz o insert no Banco de Dados.

    Argumentos:
        - data (BitcoinSchema): Schema do Pydantic validado.

    Retorno:
        - BitcoinTable: Dado validado inserido no Banco de Dados 
    """
    try:
        with SessionLocal() as session:
            db_bitcoin = BitcoinTable(**data.model_dump())
            session.add(db_bitcoin)
            session.commit()
            session.refresh(db_bitcoin)

        return None
    
    except RuntimeError:
        print("Erro ao salvar o dado no Banco de Dados.")