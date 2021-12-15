from pydantic.dataclasses import dataclass
from pydantic import StrictStr
from pydantic import BaseModel,validator
from flask import jsonify, request
import re
#recebe um dicionarios
class PersonModel(BaseModel):
    #para não converter as variaveis e seus tipos utiliza o Strict
    
    name:StrictStr
    cpf:StrictStr
    job:StrictStr

    @validator('name','cpf','job')
    def validador_create(cls,v):
        if not type(v) == str:
            raise ValueError(v," must be string")
        return v
        
    @validator('cpf')
    def validador_cpf(cls,v):
        if not re.match("[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}$", v):
            raise ValueError("cpf is invalid")
        return v

"""p={'name':'irlla','cpf':'123.123.123-12','job':'n'}
print(PersonModel(**p))"""