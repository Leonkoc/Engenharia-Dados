import time 
import requests
from tinydb import TinyDB
from datetime import datetime

url = "https://api.coinbase.com/v2/prices/spot"

def extract_dados_bitcoin():
    try:
        response = requests.get(url)
        response.raise_for_status()  
        dados = response.json()
        print("Requisição bem-sucedida")
        return dados
    except Exception as e:
        print(f"Erro: {e}")
        return None

def trasform_dados_bitcoin(dados):
    valor = dados["data"]["amount"]
    criptomoeda = dados["data"]["base"]
    moeda = dados["data"]["currency"]
    timestemp = datetime.now().timestamp()

    dados_transformados = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp": timestemp
    }

    return dados_transformados

def salvar_dados_tinydb(dados, db_name="bitcoin.json"):
    db = TinyDB(db_name)
    db.insert(dados)
    print("Dados salvos")

if __name__ == "__main__":
    while True: 
        dados_json = extract_dados_bitcoin()    
        dados_tratados = trasform_dados_bitcoin(dados_json)
        salvar_dados_tinydb(dados_tratados)
        time.sleep(15)


print(extract_dados_bitcoin()["data"])

# Estamos trabalhando com um banco noSql- que trata cada linha inserida como objeto 
