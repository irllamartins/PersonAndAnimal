from pydantic.dataclasses import dataclass
from pydantic import StrictStr
from pydantic import BaseModel,validator
from flask import jsonify, request
from src.application.domain.utils import PyObjectId
import re
#recebe um dicionarios
class AnimalModel(BaseModel):
    #para não converter as variaveis e seus tipos utiliza o Strict
    id:PyObjectId 
    name:StrictStr
    owner:StrictStr
    type:StrictStr

    @validator('name','type')
    def validador_create(cls,v):
        if not type(v) == str:
            raise ValueError(v," must be string")
        return v
        
    @validator('owner')
    def validador_owner(cls,v):
        if not re.match("[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}$", v):
            raise ValueError("owner is invalid")
        return v

"""a={'name':'toto','owner':'123.123.123-12','type':'n'}
print(AnimalModel(**a))"""