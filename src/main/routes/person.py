from typing import Collection
from flask import jsonify, request,Blueprint,Response
from pymongo import TEXT
from ...infrastructure.database.connection.mongodb import db
from bson import ObjectId
import json
from src.infrastructure.repository.person_repository import PersonReposity
from src.application.services.person_services import Sevices
from src.application.domain.models.person_model import PersonModel

person_collection=db['person']
PEOPLE=Blueprint('person',__name__)


@PEOPLE.route('/people', methods=["GET"])
def getAll():
    repository=PersonReposity(person_collection)
    person=Sevices(repository).getAll()
    return Response(json.dumps(person),status=200,content_type="application/json")

@PEOPLE.route('/people/<person_id>', methods=["GET"])
def get(person_id):
    repository=PersonReposity(person_collection)
    person=Sevices(repository).find_by_id(person_id)
    if(person==None):
        return Response(status=200)
    return  Response(json.dumps(person),status=200,content_type="application/json")

@PEOPLE.route('/people',methods=["POST"])  
def post():
    #person->PersonReposity->Services->Model
    repository=PersonReposity(person_collection)
    person=Sevices(repository).create()
    if(person!=None):
        return Response(json.dumps(person),status=201,content_type="application/json")
    else:
        return {"message":"must have name,cpf and job."}, 400

@PEOPLE.route('/people/<person_id>',methods=["PUT"])
def put(person_id):
    repository=PersonReposity(person_collection)
    person = Sevices(repository).put(person_id)
    
    if(person!=None):
        return Response(json.dumps(person),status=200,content_type="application/json")
    return Response(status=200)

@PEOPLE.route('/people/<person_id>',methods=["DELETE"])
def delete(person_id):
    repository=PersonReposity(person_collection)
    person = Sevices(repository).delete(person_id)
    if(person!=0):
        return {'mensage':'person deleted'},200
    return Response(status=200)