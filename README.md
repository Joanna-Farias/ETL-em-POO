#  ETL em Programação Orientada a Objetos

> Prática para a cadeira de Engenharia de Dados e Big Data

## Integrante do grupo
- Joanna Luciana Maria dos Santos Farias | Turma Embarque (ADS-B)

## Descrição

Projeto acadêmico desenvolvido para solucionar o problema proposto para a cadeira de Engenharia de Dados e Big Data do quarto período: evitar a criação de um código diferente para cada série, alterando apenas os parâmetros necessários para realizar cada consulta.

O pipeline segue as três etapas de um processo de ETL:

- **Extract**: consome a API do IBGE, filtrando por variável, sexo e localidade.
- **Transform**: normaliza o JSON aninhado retornado pela API em registros "achatados", trata valores ausentes/inválidos (`...`, `-`, `X`) e remove duplicidades.
- **Load**: persiste os dados tratados em três formatos possíveis, conforme a necessidade:
  - `load_json`: salva localmente em arquivo `.json`, garantindo formatação e codificação UTF-8 corretas.
  - `load_mongo`: insere os documentos em uma coleção do MongoDB (Atlas), via `pymongo`.
  - `load_sqlite`: grava os dados em um banco relacional local SQLite (`ibge.db`), a partir de um DataFrame.

Essa evolução (JSON → MongoDB → SQLite) foi proposital: permite comparar, na prática, como o mesmo dado tabular se comporta em um modelo de documentos (NoSQL) versus um modelo relacional, e qual se encaixa melhor para esse tipo de informação.

No projeto é feita a utilização da API do IBGE, extraindo indicadores da Tabela 4093: **Pessoas de 14 anos ou mais de idade, total, na força de trabalho, ocupadas, desocupadas, fora da força de trabalho, em situação de informalidade e respectivas taxas e níveis, por sexo**.

- [Link para API utilizada.](https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/201201%7C201202%7C201203%7C201204%7C201301%7C201302%7C201303%7C201304%7C201401%7C201402%7C201403%7C201404%7C201501%7C201502%7C201503%7C201504%7C201601%7C201602%7C201603%7C201604%7C201701%7C201702%7C201703%7C201704%7C201801%7C201802%7C201803%7C201804%7C201901%7C201902%7C201903%7C201904%7C202001%7C202002%7C202003%7C202004%7C202101%7C202102%7C202103%7C202104%7C202201%7C202202%7C202203%7C202204%7C202301%7C202302%7C202303%7C202304%7C202401%7C202402%7C202403%7C202404%7C202501%7C202502%7C202503%7C202504%7C202601%7C202602/variaveis/4096%7C4099%7C12466?localidades=N3%5B26%5D&classificacao=2%5Ball%5D)

## Estrutura do projeto

```
ETL-em-POO/
├── src/
│   ├── __init__.py
│   ├── extract.py     # classe Extract: acessa a API do IBGE
│   ├── transform.py   # classe Transform: normaliza, limpa e deduplica os dados
│   └── load.py        # classe Load: persiste os dados em JSON, MongoDB ou SQLite
├── jsons/              # arquivos .json gerados pelo pipeline
├── ibge.db               # banco SQLite gerado pelo load_sqlite
├── run_ETL.py              # orquestra o fluxo Extract → Transform → Load
├── requirements.txt          # dependências do projeto
├── .env                        # credenciais de conexão com o MongoDB (NÃO versionado)
└── .gitignore                    # ignora o ambiente virtual, .env e arquivos gerados
```

## Como funciona o pipeline

Utilizando como base códigos elaborados nos slides utilizados em aula, a classe `Extract` possui um método que faz requisições HTTP à API do IBGE, permitindo filtrar por variável, sexo e localidade e retorna os dados em formato JSON:

```python
import requests

class Extract():
    def __init__(self):
        pass

    def extract_pnadc(self, variavel, sexo, localidade="26"):
        url = f"https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/201201-202601/variaveis/{variavel}?localidades=N3[{localidade}]&classificacao=2[{sexo}]"
        
        response = requests.get(url)
        data = response.json()
        return data
```

A classe `Transform` recebe esse JSON aninhado e o converte em registros "achatados" (localidade, variável, sexo, período e valor), tratando valores ausentes/inválidos e eliminando duplicidades antes da carga.

A classe `Load` oferece três formas de persistir o resultado:

```python
def load_mongo(self, uni_dict, db_name, collection_name):
    uri = MONGO_URI
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    collection.insert_many(uni_dict if isinstance(uni_dict, list) else [uni_dict])
```

A credencial de conexão com o MongoDB é lida do arquivo `.env` (variável `MONGODB_URI`), nunca versionada no repositório.

No `run_ETL.py`, as classes são instanciadas e o fluxo completo (Extract → Transform → Load) é executado para as combinações de variável e sexo definidas.

## Como executar

1. Crie e ative o ambiente virtual:
   ```bash
      python -m venv .venv
      # Windows
      .venv\Scripts\activate
      # Linux/Mac
      source .venv/bin/activate
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Crie um arquivo `.env` na raiz do projeto com sua string de conexão do MongoDB:
   ```dotenv
   MONGODB_URI="mongodb+srv://<usuario>:<senha>@<cluster>.mongodb.net"
   ```

4. Execute:
   ```bash
   python run_ETL.py
   ```

## Próximos passos

- [ ] Avaliar migração da persistência para um banco relacional gerenciado (ex: NeonDB/PostgreSQL)
- [ ] Adicionar testes automatizados para as classes Extract, Transform e Load
