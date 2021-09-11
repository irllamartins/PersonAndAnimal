from sanic.response import json
from sanic import Blueprint

DEVICES=Blueprint('devices')
dispositivo={"cpf":'12312312',"id":0}
dispositivos=[]

@DEVICES.route('/devices', methods=["GET"])
async def get(request):
    return json(dispositivos)

@DEVICES.route('/devices',methods=["POST"])
async def post(request):
    if( "cpf" in request.json):
        dispositivos.append(request.json)
        return json(request.json,status=201)
    return json({"message":"corpo da requisição inválido"},status=400)

@DEVICES.route('/devices',methods=["PUT"])
async def put(request):
    return json({"message":"Not Implemented"}, status=501)

@DEVICES.route('/devices',methods=["DELETE"])
async def delete(request):
    return json({"message":"Not Implemented"}, status=501)