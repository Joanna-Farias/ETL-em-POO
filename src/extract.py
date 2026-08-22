import requests

class Extract():
    def __init__(self):
        pass

    def extract_pnadc(self, variavel, sexo, localidade="26"):
        url = f"https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/201201-202601/variaveis/{variavel}?localidades=N3[{localidade}]&classificacao=2[{sexo}]"
        
        response = requests.get(url)
        data = response.json()
        return data