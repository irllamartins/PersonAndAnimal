from sanic.response import json, text
from sanic import Blueprint
import re

PEOPLES=Blueprint('peoples')
#pessoa={"cpf":'12312312',"age":12,"name":"maria"}
peoples=[]

@PEOPLES.route('/peoples', methods=["GET"])
async def get(request):
    return json(peoples)

@PEOPLES.route('/peoples',methods=["POST"])
async def post(request):
    if( "cpf" in request.json and "age" in request.json and "name" in request.json):
        print("not in")
        if not isinstance(request.json['cpf'], str):
            return json({"message":"cpf must be string"}, status=400)
        if not re.match("[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}$", request.json['cpf']):
            return json({"message":"cpf is invalid"}, status=400)
        if not isinstance(request.json['age'], int):
            return json({"message":"age must be integer"}, status=400)
        if not isinstance(request.json['name'], str):
            return json({"message":"name must be string"}, status=400)
        for people in peoples:
            if people['cpf']==request.json['cpf']:
                return json({"message":"people already exists"}, status=409)
        people=dict(cpf=request.json['cpf'],age=request.json['age'],nome=request.json['name'])
        peoples.append(people)
        return json(people,status=201)
    return json({"message":"must have cpf, age and name."}, status=400)

@PEOPLES.route('/peoples',methods=["PUT"])
async def put(request):
    if "cpf" in request.json and ("age" in request.json or "name" in request.json):
        for index in range(len(peoples)):
            if(peoples[index]["cpf"]==request.json['cpf']):
                if "age" in request.json:
                    peoples[index]["age"]=request.json['age']
                if "name" in request.json:
                    peoples[index]["name"]=request.json['name']
                return json({**peoples[index],**request.json},status=200)
        return json({"message":"people was not found"},status=400)
    else:
        return json({"message":"corpo da requisição inválido"},status=400)


@PEOPLES.route('/peoples',methods=["DELETE"])
async def delete(request):
    if "cpf" in request.json:
        for index in range(len(peoples)):
            if(peoples[index]["cpf"]==request.json['cpf']):
                peoples.pop(index)
                return text("",status=204)
        return json({"message":"people was not found"},status=400)
    else:
        return json({"message":"cpf must be string"}, status=400) 