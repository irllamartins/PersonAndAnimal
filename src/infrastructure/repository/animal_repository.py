from src.application.domain.models.animal_model import AnimalModel
from ...infrastructure.database.connection.mongodb import db
from bson import ObjectId
from flask import request,Response
import json
"""person_collection=db['person']
animal_collection=db['animal']"""
class AnimalReposity:
    def __init__(self,person_collection,animal_collection):
        self.person_collection = person_collection
        self.animal_collection = animal_collection
        
    def find_all(self,person_id):
        result =[]
        if(self.person_collection.find_one({'_id':ObjectId(person_id)})):
            search=list(self.animal_collection.find())
            
        
            for animal in search:
                if(animal['owner']==str(self.person_collection.find_one({'_id':ObjectId(person_id)})['_id'])):
                    result.append(animal)
            return result   
        return result

    def find_by_id(self,person_id,animal_id):
        
        if(self.person_collection.find_one({'_id':ObjectId(person_id)}) and str(self.animal_collection.find_one({'_id':ObjectId(animal_id)})['owner'])==person_id  ):
            #acionar o controller???
            animal= dict(self.animal_collection.find_one({'_id':ObjectId(animal_id)}))
            
            return animal
        return
    def create(self,query,person_id):
        #verifica se o dono existe
        #animal=dict(name = request.json['name'],owner = request.json['owner'],type=request.json['type'])
        #print(animal)
        if(self.person_collection.find_one({'_id':ObjectId(person_id)})):
            self.animal_collection.insert_one(query)
            return query
        return
       
    def put(self,person_id,animal_id,update):
        #ajeitar para comparar id,validar o corpo ,models antes,deletar a chave do dono
        #controller status
        print("t1",animal_id)
        #print("animal(owner)",self.animal_collection.find_one({'_id':ObjectId(animal_id)})['owner'])
        if 'owner' in update:
            del update['owner']
        if(str(self.animal_collection.find_one({'_id':ObjectId(animal_id)})['owner'] )==person_id): 
            #sucesso ou naõ
            if(self.animal_collection.update_one({'_id':ObjectId(animal_id)},{'$set':update}).modified_count ):
                return True
                #return Response(status=204)
            return False
                #return 500
        return False
        

    def delete_by_id(self,person_id,animal_id):
        if(self.person_collection.find_one({'_id':ObjectId(person_id)}) and str(self.animal_collection.find_one({'_id':ObjectId(animal_id)})['owner'])==person_id ):
            animal= self.animal_collection.delete_one({'_id':ObjectId(animal_id)})
            return animal.deleted_count
        return 0