from flask import current_app
from . import api_routes

@api_routes.route('/')
def index():
	current_app.logger.info('/api/v1/')
	return "this is /api/v1/"