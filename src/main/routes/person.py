from ...infrastructure.database.connection.mongodb import db
from bson import ObjectId
from flask import request
#person_collection=db['person']
class PersonReposity:
    def __init__(self,person_collection):
        self.person_collection = person_collection   
      
    def find_all(self):
        search=list(self.person_collection.find())
        return search

    def find_by_id(self,person_id):
        if(self.person_collection.find_one({'_id':ObjectId(person_id)})==None):
            return 
        person=dict(self.person_collection.find_one({'_id':ObjectId(person_id)}))
        person['_id']=str(person['_id'])
        return person
        
    def create(self):
        person=dict(name = request.json['name'],cpf = request.json['cpf'],job=request.json['job'])
        self.person_collection.insert_one(person)
        person['_id']=str(person['_id'])
        return person
       
    def put(self,person_id,update):
        if(self.person_collection.update_one({'_id':ObjectId(person_id)},{'$set':update})==None): 
           return
        person=dict(self.person_collection.find_one({'_id':ObjectId(person_id)}))
        #person['_id']=str(person['_id'])
        return person

    def delete_by_id(self,person_id):
        person= self.person_collection.delete_one({'_id':ObjectId(person_id)})
        return person.deleted_count
    
