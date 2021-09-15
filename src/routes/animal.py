from sanic.response import json, text
from sanic import Blueprint
from .people import peoples

ANIMALS=Blueprint('animal')
#animal={"owner":"203.444.283-73","name":"bibi", "type":"dog"}
animals=[]

@ANIMALS.route('/animals', methods=["GET"])
async def get(request):
    return json({"message":"Not Implemented"}, status=501)

@ANIMALS.route('/animals',methods=["POST"])
async def post(request):
    return json({"message":"Not Implemented"}, status=501)

@ANIMALS.route('/animals',methods=["PUT"])
async def put(request):
    return json({"message":"Not Implemented"}, status=501)

@ANIMALS.route('/animals',methods=["DELETE"])
async def delete(request):
    return json({"message":"Not Implemented"}, status=501)