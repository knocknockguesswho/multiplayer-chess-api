from flask import Blueprint
from ...controllers.auth import AuthController

auth = Blueprint('auth', __name__)
controller = AuthController()

@auth.route('/signup', methods=['POST'])
def sign_up():
  return controller.sign_up()

@auth.route('/signin', methods=['POST'])
def sign_in():
  return controller.sign_in()