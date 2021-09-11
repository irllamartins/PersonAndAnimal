from sanic import Sanic
from src.routes import ROUTES_API

app = Sanic("api")

app.blueprint(ROUTES_API)
