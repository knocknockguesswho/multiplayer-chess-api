from flask import Flask, Blueprint
from .user import user
from .auth import auth
from ..config import config

routes = Flask(__name__)

url_prefix = '/api/v1'

routes.register_blueprint(user, url_prefix=f'{url_prefix}/user')
routes.register_blueprint(auth, url_prefix=f'{url_prefix}/auth')