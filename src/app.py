from flask import Flask
from src.main.routes import ROUTES_API
from flask import Blueprint

app = Flask(__name__)

app.register_blueprint(ROUTES_API)
