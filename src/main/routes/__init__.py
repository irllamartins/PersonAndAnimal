from flask import Blueprint
from .person import PEOPLE
from .animal import ANIMALS

ROUTES_API=Blueprint("ROUTES_API", __name__)
ROUTES_API.register_blueprint(PEOPLE)
ROUTES_API.register_blueprint(ANIMALS)