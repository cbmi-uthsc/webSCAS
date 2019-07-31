
# Import and Set
#################

from flask import Blueprint
api_routes = Blueprint('api_routes', __name__)

###############################################################################


# List of all router files
###########################

from .index import *

###############################################################################