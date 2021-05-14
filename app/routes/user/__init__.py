from flask import Blueprint, request
from ...controllers.user import UserControllers

user = Blueprint('user', __name__)
controller = UserControllers() 

@user.route('/')
def user_methods():
  return controller.get_user()

@user.route('/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def user_by_id_methods(id):
  if request.method == 'DELETE':
    return controller.delete_user(id)
  elif request.method == 'PUT':
    return controller.update_user(id)
  else:
    return controller.get_user_by_id(id)