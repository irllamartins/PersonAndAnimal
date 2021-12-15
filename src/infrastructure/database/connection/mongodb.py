from pymongo import MongoClient
from bson import ObjectId #importa o tipo ObjectId utilizado pelo mongodb na geração automática dos ids

cliente=MongoClient("mongodb://localhost:27017")#se conecta ao banco de dados
db=cliente['Teste']#cria ou acessa a database com nome 'api'
