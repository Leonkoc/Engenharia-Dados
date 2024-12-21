# Projeto ETL: Extração de Dados Bitcoin com Python e Microsoft Azure

## Introdução
Este projeto apresenta a criação de um pipeline ETL completo, explorando todas as etapas: extração, transformação e carga de dados. Utilizando a API da [Coinbase](https://docs.cdp.coinbase.com/exchange/docs/welcome) como exemplo, coletamos dados em tempo real sobre o preço do Bitcoin, transformamos essas informações em um formato tabular e as armazenamos em bancos de dados para posterior visualização.

O projeto combina o uso de bancos NoSQL, para o armazenamento inicial dos dados brutos e aqui para o NoSQL usamo o TinyDB, e SQL (PostgreSQL), para a organização e análise dos dados já processados. A consulta e gerenciamento do banco de dados SQL foram realizados com o pgAdmin, uma ferramenta de administração gráfica amplamente utilizada para PostgreSQL.

Além disso, utilizamos o serviço do [Render](https://render.com/), uma plataforma gratuita e open-source que facilita o deploy de aplicações na nuvem, para hospedar a aplicação e possibilitar o acesso remoto ao pipeline e ao dashboard.

Ao final, os dados transformados são integrados a um dashboard interativo, permitindo acompanhar as variações de preço em tempo real e facilitando análises detalhadas.

Este projeto visa demonstrar a aplicação prática de conceitos de ETL, destacando a integração entre diferentes tecnologias e a importância da análise de dados na tomada de decisão.
</br>
## Estrutura do Projeto
O pipeline segue as etapas de ETL:

1. **Extração (E):** 
   - Consome dados da API da Coinbase.
   - Obtém informações como preço do Bitcoin, horário da consulta e moeda de referência (USD).

2. **Transformação (T):**
   - Seleciona os dados relevantes.
   - Organiza as informações em um DataFrame usando **Pandas**.

3. **Carga (L):**
   - Armazena os dados transformados em um banco de dados PostgreSQL (ou localmente em um arquivo CSV).
   - Automatiza a execução do pipeline.

4. **Visualização:**
   - Criação de dashboards interativos com **Streamlit** para análise dos dados coletados.
---

## Tecnologias Utilizadas
- **Linguagem:** Python 3.12
- **Bibliotecas:**
  - `requests`: Para consumo de APIs.
  - `pandas`: Manipulação e organização de dados.
  - `psycopg2-binary`: Conexão com PostgreSQL.
  - `sqlalchemy`: Interface para banco de dados.
  - `streamlit`: Visualização de dados.
  - `time` e `datetime`: Controle de tempo e datas.
- **Banco de Dados:** PostgreSQL e TinyDB (NoSql)

---

## Como Executar
### 1. Clonar o Repositório
```bash
git clone https://github.com/Leonkoc/Engenharia-Dados.git
cd Engenharia-Dados/ETL-Completa
```
### 2. Instalar Dependências
```bash
pip install -r requirements.txt
```
### 3. Configurar Banco de Dados
* Configure as variáveis de ambiente no arquivo .env:

```bash
pip install -r requirements.txt
```
### 4. Executar o Script
Aqui configuramos a função para rodar a cada 15 segundos e com a possibilidade de para o código com ctrl + c 
```bash
python main.py
```
### 5. Visualizar Dados
* Use um dashboard interativo com Streamlit:
```bash
streamlit run dashboard.py
```

### Funcionalidades Futuras
- Transformação Avançada: Enriquecimento e análise dos dados.
- Escalabilidade: Armazenamento em serviços de nuvem como Azure.
- Alertas: Notificações para mudanças significativas no preço.
- Usar alguma ferramenta de observabilidade como a [pydantic](https://pydantic.dev/)

###  Aprendizados
Este projeto cobre:

1. Consumo de APIs públicas.
2. Manipulação de dados com Pandas.
3. Automação de pipelines ETL.
4. Visualização de dados com dashboards.

### Conclusão
```bash
Este projeto é uma introdução prática à Engenharia de Dados, abordando conceitos fundamentais com ferramentas populares.
```
## Créditos

Este projeto foi desenvolvido como parte da **Jornada de Dados**, um aprendizado adquirido durante uma aula ministrada por [Luiz Galvão](https://github.com/lvgalvao).

---
### Feito por mim:  
<div>
  <a href="https://www.linkedin.com/in/leon-ortega-cerqueira/" target="_blank">
    <img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank">
  </a>
  <br>
  <a href="https://github.com/Leonkoc" target="_blank">
    <img src="https://avatars.githubusercontent.com/u/64026100?v=4" width=115 alt="Leon Ortega GitHub Avatar">
  </a>
  <br>
  <sub><a href="https://github.com/Leonkoc" target="_blank">Leon Ortega</a></sub>
  <br>
  Caso tenha alguma dúvida ou sugestão, por favor entre em contato via <a href="mailto:leonkoc@hotmail.com">email</a>.
</div>
