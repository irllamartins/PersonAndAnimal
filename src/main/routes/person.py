import re
from typing import Collection
from flask import jsonify, request,Blueprint,Response
from pymongo import TEXT
from ...infrastructure.database.connection.mongodb import db
from bson import ObjectId
import json
person_collection=db['person']
PEOPLE=Blueprint('person',__name__)
people=[]

@PEOPLE.route('/people', methods=["GET"])
def getAll():
    search=list(person_collection.find())
    people=[]
    for person in search:
        person['_id']=str(person['_id'])
        people.append(person)
    return Response(json.dumps(person),status=200,content_type="application/json")

@PEOPLE.route('/people/<person_id>', methods=["GET"])
def get(person_id):
    
    if(person_collection.find_one({'_id':ObjectId(person_id)})==None):
        return Response(status=200)
    person=dict(person_collection.find_one({'_id':ObjectId(person_id)}))
    person['_id']=str(person['_id'])
    #print(person_collection.find_one({'_id':ObjectId(person_id)}))
    return  json.dumps(person,status=200)

@PEOPLE.route('/people',methods=["POST"])  
def post():
        
    if( "cpf" in request.json and "name" in request.json and "job" in request.json):
        print("not in")
        """if not isinstance(request.json['id_person'], str):
            return jsonify({"message":"id must be string"}, 400)
        if not isinstance(request.json['cpf'], str):
            return jsonify({"message":"cpf must be string"}, 400)
        if not re.match("[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}$", request.json['cpf']):
            return jsonify({"message":"cpf is invalid"},400)
        if not isinstance(request.json['name'], str):
            return jsonify({"message":"name must be string"}, 400)
        if not isinstance(request.json['job'], str):
            return jsonify({"message":"job must be integer"}, 400)
        for person in people:
            if person['cpf']==request.json['cpf']:
                return jsonify({"message":"person already exists"}, 409)"""
        person=dict(name = request.json['name'],cpf = request.json['cpf'],job=request.json['job'])
        #people.append(person)
        person_collection.insert_one(person)
        person['_id']=str(person['_id'])
        print(person)
        return Response(json.dumps(person),status=200,content_type="application/json")
    return {"message":"must have name,cpf and job."}, 400

@PEOPLE.route('/people/<person_id>',methods=["PUT"])
def put(person_id):
    update={}
    if "job" in request.json:
        update['job'] = request.json['job']
    if "name" in request.json:
        update['name'] = request.json['name'] 

    if(person_collection.update_one({'_id':ObjectId(person_id)},{'$set':update})): 
        person=dict(person_collection.find_one({'_id':ObjectId(person_id)}))
        person['_id']=str(person['_id'])
        print(person)
        return Response(json.dumps(person),status=200,content_type="application/json")

    return {'mensage':'person not found.'},404

@PEOPLE.route('/people/<person_id>',methods=["DELETE"])
def delete(person_id):

    print(person_collection.delete_one({'_id':ObjectId(person_id)}))
    if(person_collection.delete_one({'_id':ObjectId(person_id)})):
        return {'mensage':'person deleted'},200
        
    return {'mensage':'person not found.'},404