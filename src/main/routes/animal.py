from flask import jsonify,request,Response
from flask import Blueprint
import re
from ...infrastructure.database.connection.mongodb import db
from bson import ObjectId
from .person import person_collection
from src.infrastructure.repository.animal_repository import AnimalReposity
import json

#animal_collection=db['animal']

ANIMALS=Blueprint('animal',__name__)
animals=[]
@ANIMALS.route('/person/<person_id>/animals', methods=["GET"])
def getAll(person_id):
    search= AnimalReposity.find_all()
    result =[]
    
    for animal in search:
        animal['_id']=str(animal['_id'])
       
        if(animal['owner']==person_collection.find_one({'_id':ObjectId(person_id)})['cpf']):
            result.append(animal)
    return Response(json.dumps(animal),status=200,content_type="application/json")

@ANIMALS.route('/person/<person_id>/animals/<animal_id>', methods=["GET"])
def get(person_id,animal_id):
    #print(animal_collection.find_one({'_id':ObjectId(animal_id)}))
    animal = AnimalReposity.find_by_id(person_id,animal_id)
    if(animal!=None):
        return jsonify(animal),200
    return Response(status=200)
    
@ANIMALS.route('/person/<person_id>/animals',methods=["POST"])  
def post(person_id):
    if( "name" in request.json and "owner" in request.json and "type" in request.json):
        
        """if not isinstance(request.json['id_animal'], str):
            return jsonify({"message":"id must be string"}, 400)
        if not re.match("[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}$", request.json['owner']):
            return jsonify({"message":"cpf is invalid"},400)
        if not isinstance(request.json['name'], str):
            return jsonify({"message":"name must be string"}, 400)
        if not isinstance(request.json['type'], str):
            return jsonify({"message":"type must be integer"}, 400)
        for animal in animals:
            if animal['id_animal']==id_animal:
                return jsonify({"message":"animal already exists"}, 409)"""
        animal = AnimalReposity.create()
        Response(json.dumps(animal),status=201,content_type="application/json")

    return {"message":"must have name,owner and type."}, 400

@ANIMALS.route('/person/<person_id>/animals/<animal_id>',methods=["PUT"])
def put(person_id,animal_id):
    update={}
    if "name" in request.json:
        update['name'] = request.json['name'] 
    if "owner" in request.json:
        update['owner'] = request.json['owner']
    if "type" in request.json:
        update['type'] = request.json['type']
    
    if(animal_collection.update_one({'_id':ObjectId(animal_id)},{'$set':update})and animal_collection.find_one({'_id':ObjectId(animal_id)})['owner']==person_collection.find_one({'_id':ObjectId(person_id)})['cpf'] and animal_collection.find_one({'_id':ObjectId(animal_id)})['_id'] ): 
        animal=dict(animal_collection.find_one({'_id':ObjectId(animal_id)}))
        animal['_id']=str(animal['_id'])
        print(animal)
        return jsonify(animal),200

    return Response(status=200)
    

@ANIMALS.route('/person/<person_id>/animals/<animal_id>',methods=["DELETE"])
def delete(person_id,animal_id):

    if(AnimalReposity.delete_by_id(animal_id)!=0):
        animal_collection.delete_one({'_id':ObjectId(animal_id)})
        return {'mensage':'person deleted'},200
    return Response(status=200)
