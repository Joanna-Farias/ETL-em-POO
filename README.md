#  ETL em Programação Orientada a Objetos

> Prática para a cadeira de Engenharia de Dados e Big Data

## Integrante do grupo
- Joanna Luciana Maria dos Santos Farias | Turma Embarque (ADS-B)

## Descrição

Projeto acadêmico desenvolvido para solucionar o problema proposto para a cadeira de Engenharia de Dados e Big Data do quarto período: evitar a criação de um código diferente para cada série, alterando apenas os parâmetros necessários para realizar cada consulta.

No projeto é feita a utilização da API do IBGE, extraindo indicadores da Tabela 4093: **Pessoas de 14 anos ou mais de idade, total, na força de trabalho, ocupadas, desocupadas, fora da força de trabalho, em situação de informalidade e respectivas taxas e níveis, por sexo**.

- [Link para API utilizada.](https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/201201|201202|201203|201204|201301|201302|201303|201304|201401|201402|201403|201404|201501|201502|201503|201504|201601|201602|201603|201604|201701|201702|201703|201704|201801|201802|201803|201804|201901|201902|201903|201904|202001|202002|202003|202004|202101|202102|202103|202104|202201|202202|202203|202204|202301|202302|202303|202304|202401|202402|202403|202404|202501|202502|202503|202504|202601|202602/variaveis/4096|4099|12466?localidades=N3[26]&classificacao=2[all])

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
