from sanic.response import json, text
from sanic import Blueprint

BODY_PRESENCE=Blueprint('body_presence')
dispositivo={"cpf":'12312312',"id":0}
dispositivos=[]

@BODY_PRESENCE.route('/bodypresence', methods=["GET"])
async def get(request):
    return json({"message":"Not Implemented"}, status=501)

@BODY_PRESENCE.route('/bodypresence',methods=["POST"])
async def post(request):
    return json({"message":"Not Implemented"}, status=501)

@BODY_PRESENCE.route('/bodypresence',methods=["PUT"])
async def put(request):
    return json({"message":"Not Implemented"}, status=501)

@BODY_PRESENCE.route('/bodypresence',methods=["DELETE"])
async def delete(request):
    return json({"message":"Not Implemented"}, status=501)