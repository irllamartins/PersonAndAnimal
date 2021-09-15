from sanic import Blueprint
from .people import PEOPLES
from .animal import ANIMALS

ROUTES_API=Blueprint.group(PEOPLES, ANIMALS)