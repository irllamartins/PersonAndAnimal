import re
from typing import Collection
from flask import jsonify, request,Blueprint,Response
from pymongo import TEXT
from ...infrastructure.database.connection.mongodb import db
from bson import ObjectId
import json
from src.infrastructure.repository.person_repository import PersonReposity
person_collection=db['person']
PEOPLE=Blueprint('person',__name__)


@PEOPLE.route('/people', methods=["GET"])
def getAll():
    search=PersonReposity(person_collection).find_all()
    #print(search)
    #search=search.find_all()
    people=[]
    for person in search:
        person['_id']=str(person['_id'])
        people.append(person)
    return Response(json.dumps(person),status=200,content_type="application/json")

@PEOPLE.route('/people/<person_id>', methods=["GET"])
def get(person_id):
    person=PersonReposity(person_collection).find_by_id(person_id)
    if(person==None):
        return Response(status=200)
    return  Response(json.dumps(person),status=200,content_type="application/json")

@PEOPLE.route('/people',methods=["POST"])  
def post():
        
    if( "cpf" in request.json and "name" in request.json and "job" in request.json):
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
       
        person=PersonReposity(person_collection).create()
        #print(person)
        return Response(json.dumps(person),status=201,content_type="application/json")
    return {"message":"must have name,cpf and job."}, 400

@PEOPLE.route('/people/<person_id>',methods=["PUT"])
def put(person_id):
    update={}
    if "job" in request.json:
        update['job'] = request.json['job']
    if "name" in request.json:
        update['name'] = request.json['name'] 
    person = PersonReposity(person_collection).put(person_id,update)
    person['_id']=str(person['_id'])
    if(person!=None):
        return Response(json.dumps(person),status=200,content_type="application/json")
    return {'mensage':'person not found.'},404

@PEOPLE.route('/people/<person_id>',methods=["DELETE"])
def delete(person_id):
    if(PersonReposity(person_collection).delete_by_id(person_id)!=0):
        return {'mensage':'person deleted'},200
    return Response(status=200)
