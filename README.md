# ETL em Programação Orientada a Objetos

Prática para a cadeira de Engenharia de Dados e Big Data

## Integrante do grupo
- Joanna Luciana Maria dos Santos Farias | Turma Embarque (ADS-B)

## Descrição

Projeto acadêmico desenvolvido para solucionar o problema proposto para a cadeira de Engenharia de Dados e Big Data do quarto período: evitar a criação de um código diferente para cada série, alterando apenas os parâmetros necessários para realizar cada consulta.

O pipeline segue as três etapas clássicas de um processo de ETL:

- **Extract**: consome a API do IBGE, extraindo indicadores da Tabela 4093 (*Pessoas de 14 anos ou mais de idade, total, na força de trabalho, ocupadas, desocupadas, fora da força de trabalho, em situação de informalidade e respectivas taxas e níveis, por sexo*).
- **Transform**: normaliza o JSON aninhado retornado pela API, trata valores ausentes/inválidos e remove duplicidades, deixando os dados prontos para carga.
- **Load**: persiste os dados tratados em banco de dados [AJUSTAR: SQLite (ibge.db) ou PostgreSQL — confirme qual está valendo hoje], além de manter um log dos dados em JSON.

- [Link para API utilizada.](https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/201201%7C201202%7C201203%7C201204%7C201301%7C201302%7C201303%7C201304%7C201401%7C201402%7C201403%7C201404%7C201501%7C201502%7C201503%7C201504%7C201601%7C201602%7C201603%7C201604%7C201701%7C201702%7C201703%7C201704%7C201801%7C201802%7C201803%7C201804%7C201901%7C201902%7C201903%7C201904%7C202001%7C202002%7C202003%7C202004%7C202101%7C202102%7C202103%7C202104%7C202201%7C202202%7C202203%7C202204%7C202301%7C202302%7C202303%7C202304%7C202401%7C202402%7C202403%7C202404%7C202501%7C202502%7C202503%7C202504%7C202601%7C202602/variaveis/4096%7C4099%7C12466?localidades=N3%5B26%5D&classificacao=2%5Ball%5D)

## Estrutura do projeto

```
ETL-em-POO/
├── src/
│   ├── __init__.py
│   ├── extract.py     # classe Extract: acessa a API do IBGE
│   ├── transform.py   # classe Transform: normaliza, limpa e deduplica os dados
│   └── load.py        # classe Load: salva os dados tratados em JSON e no banco
├── jsons/              # saídas em JSON geradas pelo pipeline (extração bruta e/ou tratada)
├── notebooks/           # notebook(s) de exploração/validação dos dados (aula1.ipynb)
├── ibge.db              # banco [AJUSTAR: SQLite] com os dados já carregados
├── main.py               # orquestra o fluxo Extract → Transform → Load
├── requirements.txt        # dependências do projeto
├── .env                     # credenciais de conexão com o banco (NÃO versionado)
└── .gitignore                # ignora .venv, __pycache__, .env e arquivos temporários
```

## Como funciona o pipeline

A classe `Extract` faz requisições HTTP à API do IBGE, permitindo filtrar por variável, sexo e localidade e retorna os dados em formato JSON:

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

A classe `Transform` recebe esse JSON aninhado e o converte em registros "achatados" (um dicionário por linha), tratando valores ausentes (`...`, `-`, `X`) e removendo duplicidades antes da carga.

A classe `Load` recebe os registros tratados e os persiste [AJUSTAR: descreva aqui exatamente o que seu load.py faz hoje — grava no ibge.db via SQLite? Mantém o JSON como log?].

No `main.py`, as três classes são instanciadas e o fluxo completo é executado para as combinações de variável e sexo definidas.

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

3. [AJUSTAR: se usar banco com credenciais, adicionar aqui: "Copie .env.example para .env e preencha suas credenciais"]

4. Execute:
   ```bash
   python main.py
   ```

## Próximos passos

- [ ] Adicionar testes automatizados para as classes Extract, Transform e Load
- [ ] Documentar o schema da tabela no banco
- [ ] Incluir persistência em banco de dados relacional.