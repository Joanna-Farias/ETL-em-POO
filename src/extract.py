import requests
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv


class Extract():
    UFS = {
        11: "Rondônia",
        12: "Acre",
        13: "Amazonas",
        14: "Roraima",
        15: "Pará",
        16: "Amapá",
        17: "Tocantins",
        21: "Maranhão",
        22: "Piauí",
        23: "Ceará",
        24: "Rio Grande do Norte",
        25: "Paraíba",
        26: "Pernambuco",
        27: "Alagoas",
        28: "Sergipe",
        29: "Bahia",
        31: "Minas Gerais",
        32: "Espírito Santo",
        33: "Rio de Janeiro",
        35: "São Paulo",
        41: "Paraná",
        42: "Santa Catarina",
        43: "Rio Grande do Sul",
        50: "Mato Grosso do Sul",
        51: "Mato Grosso",
        52: "Goiás",
        53: "Distrito Federal",
    }

    VARIAVEIS_PNADC = {
        1641: "Pessoas de 14 anos ou mais de idade",
        4087: "Coeficiente de variação - Pessoas de 14 anos ou mais de idade",
        4104: "Distribuição percentual das pessoas de 14 anos ou mais de idade",
        4105: "Coeficiente de variação - Distribuição percentual das pessoas de 14 anos ou mais de idade",
        4088: "Pessoas de 14 anos ou mais de idade, na força de trabalho, na semana de referência",
        4089: "Coeficiente de variação - Pessoas de 14 anos ou mais de idade, na força de trabalho",
        4106: "Distribuição percentual das pessoas de 14 anos ou mais de idade, na força de trabalho",
        4107: "Coeficiente de variação - Distribuição percentual das pessoas de 14 anos ou mais de idade, na força de trabalho",
        4090: "Pessoas de 14 anos ou mais de idade ocupadas na semana de referência",
        4091: "Coeficiente de variação - Pessoas de 14 anos ou mais de idade ocupadas",
        4108: "Distribuição percentual das pessoas de 14 anos ou mais de idade ocupadas",
        4109: "Coeficiente de variação - Distribuição percentual das pessoas de 14 anos ou mais de idade ocupadas",
        4092: "Pessoas de 14 anos ou mais de idade, desocupadas na semana de referência",
        4093: "Coeficiente de variação - Pessoas de 14 anos ou mais de idade, desocupadas",
        4110: "Distribuição percentual das pessoas de 14 anos ou mais de idade, desocupadas",
        4111: "Coeficiente de variação - Distribuição percentual das pessoas de 14 anos ou mais de idade, desocupadas",
        4094: "Pessoas de 14 anos ou mais de idade, fora da força de trabalho",
        4095: "Coeficiente de variação - Pessoas de 14 anos ou mais de idade, fora da força de trabalho",
        4112: "Distribuição percentual das pessoas de 14 anos ou mais de idade, fora da força de trabalho",
        4113: "Coeficiente de variação - Distribuição percentual das pessoas de 14 anos ou mais de idade, fora da força de trabalho",
        4096: "Taxa de participação na força de trabalho",
        4100: "Coeficiente de variação - Taxa de participação na força de trabalho",
        4097: "Nível da ocupação",
        4101: "Coeficiente de variação - Nível da ocupação",
        4098: "Nível da desocupação",
        4102: "Coeficiente de variação - Nível de desocupação",
        4099: "Taxa de desocupação",
        4103: "Coeficiente de variação - Taxa de desocupação",
        12466: "Taxa de informalidade das pessoas de 14 anos ou mais de idade ocupadas",
        12467: "Coeficiente de variação - Taxa de informalidade das pessoas ocupadas",
        4723: "Pessoas de 14 anos ou mais de idade ocupadas, em situação de informalidade",
        4724: "Coeficiente de variação - Pessoas de 14 anos ou mais de idade ocupadas, em situação de informalidade",
    }

    def agregado(
        self,
        agregado_id: int,
        variavel: int,
        estado: int,
        periodo_inicio: str,
        periodo_fim: str,
        classificacao: str = "2[all]",
    ) -> list[dict]:
        """
        Busca, na API de agregados do IBGE, a série histórica de uma
        variável de um agregado (tabela) qualquer, para uma UF.

        Atributos:
            agregado_id: código do agregado (tabela) do IBGE
            variavel: código da variável do agregado
            estado: código IBGE da UF (ver `Extract.UFS`)
            periodo_inicio: início do período da série, no formato AAAAMM
            periodo_fim: fim do período da série, no formato AAAAMM
            classificacao: classificação/categoria da consulta (padrão: "2[all]")
        """
        

    def __init__(self):
        pass

    def pnadc(self):
        url = "https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/201201|201202|201203|201204|201301|201302|201303|201304|201401|201402|201403|201404|201501|201502|201503|201504|201601|201602|201603|201604|201701|201702|201703|201704|201801|201802|201803|201804|201901|201902|201903|201904|202001|202002|202003|202004|202101|202102|202103|202104|202201|202202|202203|202204|202301|202302|202303|202304|202401|202402|202403|202404|202501|202502|202503|202504|202601|202602/variaveis/4096|4099|12466"

        params = {
            "localidades": "N1[all]|N3[26]",
            "classificacao": "2[all]"
        }

        r = requests.get(url, params=params)
        
        if r.status_code == 200:
            print("Ok")
            print(r.url)
            data = r.json()
            return data
        else:
            print("Houve algum erro na API")
            return None
 