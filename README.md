#  ETL em Programação Orientada a Objetos

> Prática para a cadeira de Engenharia de Dados e Big Data

## Descrição

Este projeto consome a API de Agregados do IBGE para extrair
indicadores da **Tabela 4093 — Pessoas de 14 anos ou mais de idade, total,
na força de trabalho, ocupadas, desocupadas, fora da força de trabalho, em
situação de informalidade e respectivas taxas e níveis, por sexo**.

A solução foi adaptada a partir de códigos elaborados em aula para cumprir o
desafio: evitar a criação de um código diferente para cada série, alterando apenas os parâmetros necessários para realizar cada consulta.



## Estrutura do projeto

```
projeto-integrador-ibge/
├── src/
│   ├── __init__.py
│   ├── extract.py   # classe Extract: acessa a API do IBGE
│   └── load.py       # classe Load: salva os dados extraídos em JSON
├── main.py            # executa a extração para estados/variáveis/sexo
├── .gitignore          # ignora o ambiente virtual e os arquivos json
                            para evitar o risco de subir junto
```

## Como funciona a reutilização

A classe `Extract` possui um método que faz requisições HTTP à API do IBGE, permitindo filtrar por variável, sexo e localidade e retorna os dados em formato JSON:

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

A classe `Load` contém um método que recebe os dados extraídos e os salva localmente em arquivos .json, garantindo a formatação e a codificação UTF-8 corretas.

No bloco principal, na `Main`, é instanciada as classes e feita a execução do fluxo para três extrações distintas.


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

3. Execute:
   ```bash
   python main.py
   ```
