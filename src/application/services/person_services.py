from flask import  request
from bson import ObjectId
from src.application.domain.models.person_model import PersonModel

"""criar classe , instancia dependencia no init(repository),validação,compositer(retornar servises[o certo é controller]), """

class Sevices:
    #ajeitar o model: comocar um argumento modal e injetar
    def __init__(self,repository):
        self.repository = repository
        self.PersonModel= PersonModel
      
    def getAll(self):
        search=self.repository.find_all()
        
        people=[]
        for person in search:
            person['_id']=str(person['_id'])
            people.append(person)
        return people
    def find_by_id(self,person_id):
        person=self.repository.find_by_id(person_id)
        person['_id']=str(person['_id'])
        return person
    
    def create(self):
        # request.json
        #print(PersonModel(**person))
        #validar 
        person=self.repository.create()  
       
        if(person!=None):
            person['_id']=str(person['_id'])
            return person
        person=None
        return person
    
    def put(self,person_id):
        update={}
        if "job" in request.json:
            update['job'] = request.json['job']
        if "name" in request.json:
            update['name'] = request.json['name'] 

        person=self.repository.put(person_id,update)
        person['_id']=str(person['_id'])
        return person
    
    def delete(self,person_id):
        person = self.repository.delete_by_id(person_id)
        return person