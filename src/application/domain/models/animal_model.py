from bson.objectid import ObjectId
from pydantic.dataclasses import dataclass
from pydantic import StrictStr,BaseModel,validator,Field
from flask import jsonify, request
from src.application.domain.utils import PyObjectId
from typing import Optional
import re
#recebe um dicionarios
class AnimalModel(BaseModel):
    #para não converter as variaveis e seus tipos utiliza o Strict
    id:Optional[PyObjectId]=Field(alias='_id')
    name:StrictStr
    owner:StrictStr
    type:StrictStr

    @validator('name','type','owner')
    def validador_create(cls,v):
        if not type(v) == str:
            raise ValueError(v," must be string")
        return v
    @validator('id',pre=True)
    def validador_id(cls,v):
        print(type(v),"|",v)
        return v

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True  # required for the _id
        json_encoders = {ObjectId: str}
        
"""a={'name':'toto','owner':'123.123.123-12','type':'n'}
print(AnimalModel(**a))"""