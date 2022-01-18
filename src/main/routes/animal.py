from flask import jsonify,request,Response
from flask import Blueprint
from ...infrastructure.database.connection.mongodb import db
from bson import ObjectId
from .person import person_collection
from src.infrastructure.repository.animal_repository import AnimalReposity
from src.application.services.animal_services import Sevices

import json

animal_collection=db['animal']

ANIMALS=Blueprint('animal',__name__)
animals=[]
@ANIMALS.route('/person/<person_id>/animals', methods=["GET"])
def getAll(person_id):
    repository=AnimalReposity(person_collection,animal_collection)
    search= Sevices(repository).getAll(person_id)
    
    return Response(json.dumps(search),status=200,content_type="application/json")

@ANIMALS.route('/person/<person_id>/animals/<animal_id>', methods=["GET"])
def get(person_id,animal_id):
    repository=AnimalReposity(person_collection,animal_collection)
    animal = Sevices(repository).find_by_id(person_id,animal_id)
    if(animal!=None):
        return jsonify(animal),200
    return Response(status=200)
    
@ANIMALS.route('/person/<person_id>/animals',methods=["POST"])  
def post(person_id):
    repository=AnimalReposity(person_collection,animal_collection)
    animal=Sevices(repository).create(person_id)
    if(animal!=None):
        return Response(json.dumps(animal),status=201,content_type="application/json")
    else:
        return {"message":"must have name,cpf and job."}, 400

@ANIMALS.route('/person/<person_id>/animals/<animal_id>',methods=["PUT"])
def put(person_id,animal_id):
    repository=AnimalReposity(person_collection,animal_collection)
    validation = Sevices(repository).put(person_id,animal_id)
    #repensar variavel
    if(validation!=False):
        return Response(json.dumps(validation),status=200,content_type="application/json")
    return Response(status=200)
    

@ANIMALS.route('/person/<person_id>/animals/<animal_id>',methods=["DELETE"])
def delete(person_id,animal_id):
    repository=AnimalReposity(person_collection,animal_collection)
    animal = Sevices(repository).delete(person_id,animal_id)
    if(animal!=0):
         return {'mensage':'animal deleted'},200
    return Response(status=200)