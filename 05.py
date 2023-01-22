#Escreva a função obter_colecao_mongodb(url_conexao, colecao) que irá se
#conectar no MogodDB utilizando alguma biblioteca do Python. Ela possui os
#seguintes parâmetros:
#○ url_conexao: URI de conexão com banco de dados MongoDB, que também
#informa a base de dados (database). Por exemplo: a URI
#`mongodb://localhost/bancoexemplo', é a string de conexão para o banco
#"bancoexemplo" da minha máquina local ("localhost").
#○ colecao: É o nome da coleção (collection) do MongoDB que estaremos
#acessando com esta função.

import pymongo
from pymongo import MongoClient
def get_database():
 
 
   CONNECTION_STRING = pymongo.MongoClient("mongodb://localhost:27017/")

 
  
   client = MongoClient(CONNECTION_STRING)
 
   return client['user_shopping_list']

if __name__ == "__main__":   
  

   dbname = get_database()