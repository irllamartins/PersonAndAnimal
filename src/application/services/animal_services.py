from flask import  request
from src.application.domain.models.animal_model import AnimalModel

"""criar classe , instancia dependencia no init(repository),validação,compositer(retornar servises[o certo é controller]), """

class Sevices:
    def __init__(self,repository):
        self.repository = repository
      
    def getAll(self,person_id):
        search=self.repository.find_all(person_id)
        
        animals=[]
        for animal in search:
            animal['_id']=str(animal['_id'])
            animals.append(animal)
        return animals
    def find_by_id(self,person_id,animal_id):
        animal=self.repository.find_by_id(person_id,animal_id)
        animal['_id']=str(animal['_id'])
        return animal
    
    def create(self,person_id):
        animal=self.repository.create(person_id)
        if(animal!=None):
            animal['_id']=str(animal['_id'])
            return animal
        animal=None
        return animal
    
    def put(self,person_id,animal_id):
        update={}
        if "job" in request.json:
            update['type'] = request.json['type']
        if "name" in request.json:
            update['name'] = request.json['name'] 

        animal=self.repository.put(person_id,animal_id,update)
        animal['_id']=str(animal['_id'])
        return animal
    
    def delete(self,person_id,animal_id):
        animal = self.repository.delete_by_id(person_id,animal_id)
        return animal