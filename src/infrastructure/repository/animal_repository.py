from src.application.domain.models.animal_model import AnimalModel
from ...infrastructure.database.connection.mongodb import db
from bson import ObjectId
from flask import request
"""person_collection=db['person']
animal_collection=db['animal']"""
class AnimalReposity:
    def __init__(self,person_collection,animal_collection):
        self.person_collection = person_collection
        self.animal_collection = animal_collection
    def find_all(self,person_id):
        search=list(self.animal_collection.find())
        result =[]
    
        for animal in search:
            if(animal['owner']==self.person_collection.find_one({'_id':ObjectId(person_id)})['cpf']):
                result.append(animal)
        #print(result)
        return result

    def find_by_id(self,person_id,animal_id):
        
        if(self.animal_collection.find_one({'_id':ObjectId(animal_id)})['owner']==self.person_collection.find_one({'_id':ObjectId(person_id)})['cpf'] and self.animal_collection.find_one({'_id':ObjectId(animal_id)})['_id']):
            animal= dict(self.animal_collection.find_one({'_id':ObjectId(animal_id)}))
            
            return animal
        return
    def create(self,person_id):
        animal=dict(name = request.json['name'],owner = request.json['owner'],type=request.json['type'])
        print(animal)
        print(AnimalModel(**animal))
        if(self.person_collection.find_one({'_id':ObjectId(person_id)})):
            self.animal_collection.insert_one(animal)
            return animal
        return
       
    def put(self,person_id,animal_id,update):
        #ajeitar para comparar id,validar o corpo ,models antes
        #controller status
        print(AnimalModel(**animal))
        if(person_id==self.animal_collection.find_one({'_id':ObjectId(animal_id)})['owner']): 
            self.animal_collection.update_one({'_id':ObjectId(animal_id)},{'$set':update})    
            #sucesso ou naõ
            '''if():
                return 204
            else:
                return 500'''
        return
        

    def delete_by_id(self,person_id,animal_id):
        if(self.person_collection.find_one({'_id':ObjectId(person_id)})['cpf']==self.animal_collection.find_one({'_id':ObjectId(animal_id)})['owner']):
            animal= self.animal_collection.delete_one({'_id':ObjectId(animal_id)})
            return animal.deleted_count
        return 0