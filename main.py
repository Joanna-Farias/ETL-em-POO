from src.extract import Extract
from src.load import Load

extract = Extract()
load = Load()

dados_participacao = extract.extract_pnadc(variavel="4096", sexo="4")
load.load_json("taxa_participacao_homens", dados_participacao)

dados_informalidade = extract.extract_pnadc(variavel="12466", sexo="6794")
load.load_json("taxa_informalidade_total", dados_informalidade)

dados_desocupacao = extract.extract_pnadc(variavel="4099", sexo="5")
load.load_json("taxa_desocupacao_mulheres", dados_desocupacao)