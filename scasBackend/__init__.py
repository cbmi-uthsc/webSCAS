from flask import abort, Flask, request

from scasBackend.utils import get_instance_folder_path
from scasBackend.api_routes import *
from scasBackend.config import configure_app
from scasBackend.models import db
from flask_cors import CORS


app = Flask(
    __name__,
    instance_path=get_instance_folder_path(),
    instance_relative_config=True)

configure_app(app) # load configurations
db.init_app(app) # init app to db
CORS(app) #Cross Origin Resource Sharing Plugin

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('Page not found: %s', (request.path, error))
    return "404"

@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return "500"

@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.exception(error)
    app.logger.error('Unhandled Exception: %s', (error))
    return "500"

@app.before_first_request
def initialize_database():
    db.create_all()

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/')
@app.route('/<lang_code>/')
def home(lang_code=None):
    return "homepage"
    abort(404)


# register all routes
app.register_blueprint(api_routes, url_prefix='/api/v1')

###############################################################################
