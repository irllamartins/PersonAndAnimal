from typing import Optional,Tuple
from src.application.services.person_services import Sevices

class PersonController:
    def __init__(self,service):
        self.service = service
    
    def getAll(self):
        result = self.service()
        return result,200