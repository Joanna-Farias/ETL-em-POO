import sqlite3
from src.extract import Extract
import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")

class Load():
    def __init__(self):
        pass

    def load_json(self, file_name: str, data:list):
        """
        Função para salvar os dados em um arquivo JSON.
        :param file_name: Nome do arquivo (sem extensão) onde os dados serão salvos
        :param data: Lista de dados a serem salvos no arquivo JSON
        :return: None
        """
        with open(f"jsons/{file_name}.json", "w", encoding="UTF-8") as f:
                # "with": é um gerenciador de contexto, que garante que o arquivo seja fechado corretamente ao final do bloco.
                # open: abre, ou cria se não existir, um arquivo na mesma pasta do script
                json.dump(data, f, indent=2, ensure_ascii=False)
                # json dump: escreve diretamente em um arquivo (f)
                # "json.dump(...)": pega a lista "data" e escreve dentro do arquivo f, em JSON.
                # indent = 2: formata o JSON com 2 espaços de indentação, para ficar mais legível.
                # ensure_ascii=False: permite que caracteres não ASCII (como acentos) sejam escritos corretamente no arquivo.
        
    def load_mongo(self, uni_dict, db_name, collection_name):
        """
        Função para salvar os dados em uma coleção do MongoDB.
        :param uni_dict: Dicionário com os dados a serem salvos
        :param db_name: Nome do banco de dados
        :param collection_name: Nome da coleção
        :return: None
        
        """
        uri = MONGO_URI

        client = MongoClient(uri, server_api=ServerApi('1'))

        db = client[db_name]
        collection = db[collection_name]


        if uni_dict:
            if isinstance(uni_dict, list):
                collection.insert_many(uni_dict)
                print(f"Documentos inseridos na coleção {collection.name}.")
            else:
                 collection.insert_many([uni_dict])
                 print(f"Documento inserido na coleção {collection.name}.")
        else:
             print("O dicionário está vazio. Nenhum documento foi inserido.")


    def load_sqlite(self, df, db_name, table_name):
        """
        Função para salvar os dados em um banco de dados SQLite.
        :param df: DataFrame com os dados a serem salvos
        :param db_name: Nome do banco de dados SQLite
        :param table_name: Nome da tabela onde os dados serão salvos
        :return: None
        """

        conn = sqlite3.connect('ibge.db')
        df.to_sql('pnadc', conn, if_exists='replace', index=False)
        conn.close()