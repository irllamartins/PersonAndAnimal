from presenters.controllers import person_controller
from src.application.services.person_services import Sevices
from src.application.domain.models.person_model import  PersonModel
from src.infrastructure.repository.person_repository import PersonReposity

def register_person_composer():
    repository=PersonReposity(person_collection)
    person_service = Sevices(repository).getAll()
    register_person = person_controller(person_service)
    return register_person