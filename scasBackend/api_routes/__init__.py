from flask import Blueprint
api_routes = Blueprint('api_routes', __name__)

from .index import *