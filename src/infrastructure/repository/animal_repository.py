from ...infrastructure.database.connection.mongodb import db
from bson import ObjectId
from flask import request
person_collection=db['person']
animal_collection=db['animal']
class AnimalReposity:
    def __init__(self,person_collection,animal_collection):
        self.person_collection = person_collection
        self.animal_collection = animal_collection
    def find_all():
        search=list(animal_collection.find())
        #print(search)
        return search

    def find_by_id(person_id,animal_id):
        if(animal_collection.find_one({'_id':ObjectId(animal_id)})['owner']==person_collection.find_one({'_id':ObjectId(person_id)})['cpf'] and animal_collection.find_one({'_id':ObjectId(animal_id)})['_id']):
            animal= dict(animal_collection.find_one({'_id':ObjectId(animal_id)}))
            animal['_id']=str(animal['_id'])
            return animal
        return
    def create():
        animal=dict(name = request.json['name'],owner = request.json['owner'],type=request.json['type'])
        animal_collection.insert_one(animal)
        animal['_id']=str(animal['_id'])
        return animal
       
    def put(animal_id,update):
        if(animal_collection.update_one({'_id':ObjectId(animal_id)},{'$set':update})==None): 
           return
        animal=dict(animal_collection.find_one({'_id':ObjectId(animal_id)}))
        #animal['_id']=str(animal['_id'])
        return animal

    def delete_by_id(animal_id):
        animal= animal_collection.delete_one({'_id':ObjectId(animal_id)})
        return animal.deleted_count
    