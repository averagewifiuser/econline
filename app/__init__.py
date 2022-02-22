from flask import Flask
from .extensions import *
import os

#importing the routes
from .routes import main
from .admin.routes import admin

#importing errorhandlers
from .errorhandlers import *


def is_in_development():
    return not os.getenv('SERVER_SOFTWARE', '').startswith('Product Config')

def create_app():
    app = Flask(__name__)

    if is_in_development():
        app.config.from_object('config.DevelopmentConfig')
    else:
        app.config.from_object('config.ProdutionConfig')

    #initialize the extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.blueprint_login_views = {
    'admin' : '/admin/login'
    }
    migrate.init_app(app, db)


    #registering blueprints
    app.register_blueprint(main)
    app.register_blueprint(admin, url_prefix='/admin')

    #register the errorhandlers
    app.register_error_handler(500, internal_server_error)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(403, forbidden)
    app.register_error_handler(405, method_not_allowed)


    return app