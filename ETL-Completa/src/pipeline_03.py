import os
import time 
import requests
from dotenv import load_dotenv
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from database import Base, BitcoinPreco

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Lê as variáveis separadas do arquivo .env (sem SSL)
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Monta a URL de conexão ao banco PostgreSQL (sem ?sslmode=...)
DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

# Cria o engine e a sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def criar_tabela():
    """Cria a tabela no banco de dados, se não existir."""
    Base.metadata.create_all(engine)
    print("Tabela criada/verificada com sucesso!")  

url = "https://api.coinbase.com/v2/prices/spot"

def extract_dados_bitcoin():
    """Extrai os dados da API da Coinbase."""
    try:
        response = requests.get(url)
        response.raise_for_status()  
        dados = response.json()
        print("Requisição bem-sucedida")
        return dados
    except Exception as e:
        print(f"Erro ao buscar dados da API: {e}")
        return None

def transform_dados_bitcoin(dados):
    """Transforma os dados extraídos em um formato adequado para o banco."""
    valor = float(dados["data"]["amount"])
    criptomoeda = dados["data"]["base"]
    moeda = dados["data"]["currency"]
    # Converte o timestamp Unix para datetime
    timestamp = datetime.now()

    dados_transformados = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp": timestamp  # Envia datetime diretamente
    }

    return dados_transformados

def salvar_dados_postgres(dados):
    """Salvando os dados no banco PostgreSQL."""
    session = Session()
    try:
        novo_registro = BitcoinPreco(**dados)
        session.add(novo_registro)
        session.commit()
        print(f"[{dados['timestamp']}] Dados salvos no banco PostgreSQL!")
    except Exception as e:
        print(f"Erro ao salvar os dados no banco: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    criar_tabela()
    print("Iniciando ETL com atualização a cada 15 segundos... (CTRL+C para interromper)")

    while True:
        try:
            dados_json = extract_dados_bitcoin()
            if dados_json:
                dados_tratados = transform_dados_bitcoin(dados_json)
                print("Dados Tratados:", dados_tratados)
                salvar_dados_postgres(dados_tratados)
            time.sleep(15)
        except KeyboardInterrupt:
            print("\nProcesso interrompido pelo usuário. Finalizando...")
            break
        except Exception as e:
            print(f"Erro durante a execução: {e}")
            time.sleep(15)
