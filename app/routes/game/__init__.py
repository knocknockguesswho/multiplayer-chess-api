from flask import Blueprint, request
from ...controllers.game import GameControllers

game = Blueprint('game', __name__)
controller = GameControllers()

@game.route('/create', methods=['POST'])
def create_game_room():
  return controller.create_game_room()

@game.route('/<string:id>', methods=['GET', 'POST', 'PUT'])
def game_room_by_id(id):
  if request.method == 'GET':
    return controller.get_game_room_by_id(id)
  elif request.method == 'PUT':
    return controller.update_game_room_by_id(id)