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
        #by_alis vai pegar o _id e colocar no id
        query=AnimalModel(**request.json).dict(by_alias=True,exclude={'id'})
        #print(query)
        animal=self.repository.create(query,person_id)
        if(animal!=None):
            animal['_id']=str(animal['_id'])
            return animal
        animal=None
        return animal
    
    def put(self,person_id,animal_id):
        
        update=AnimalModel(**request.json).dict(by_alias=True,exclude={'id'})
        validation=self.repository.put(person_id,animal_id,update)
        print("services:",validation)
        return validation
    
    def delete(self,person_id,animal_id):

        animal = self.repository.delete_by_id(person_id,animal_id)
        print(animal)
        return animal