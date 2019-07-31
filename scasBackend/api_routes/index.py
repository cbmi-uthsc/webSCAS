
# Imports
##########

from flask import current_app
from . import api_routes

###############################################################################

# Routes
#########

@api_routes.route('/')
def index():
	current_app.logger.info('/api/v1/')
	return "this is /api/v1/"

###############################################################################
