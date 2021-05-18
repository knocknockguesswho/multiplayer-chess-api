from flask import Flask, request
from bson.objectid import ObjectId
from pymongo import ReturnDocument
from ...connection import db
from ...helpers import ResponseHelper
from ...constants import dummy_board_detail

response_helper = ResponseHelper()

class GameControllers():

  #POST
  def create_game_room(self):
    try:
      game_data = {
        'members': {'white': [request.form['white']], 'black': [request.form['black']]}, # { white: [user_id], black: [user_id] } IS_REQUIRED at least 1 user each sides
        'board_detail': [], # board detail list
        'ended_at': '', # time of game ended. set by update method later
        'winner': -1  # white or black side. set by update method later. enum = ongoing: -1 white: 0, black: 1, draw: 2
      }
      db.game.insert_one(game_data)
      game_data['_id'] = str(game_data['_id'])
      return response_helper.success_response('Success create game', game_data)
    except Exception as err:
      msg = str(err)
      print(msg)
      return response_helper.fail_response(msg)

  # GET
  def get_game_room_by_id(self, id):
    try:
      game_data = db.game.find_one({'_id': ObjectId(id)})
      game_data['created_at'] = str(game_data['_id'].generation_time)
      game_data['_id'] = str(game_data['_id'])
      return response_helper.success_response('Success get game by id', game_data)
    except Exception as err:
      msg = str(err)
      print(msg)
      if err.__cause__ == None:
        msg = f'Cannot find data with id: {id}'
      return response_helper.fail_response(msg, 500)

  #UPDATE
  ### game_room is the source and destination of game realtime data
  def update_game_room_by_id(self, id):
    try:
      game_data = db.game.find_one_and_update(
        {'_id': ObjectId(id)},
        {'$set': {'board_detail': dummy_board_detail, 'ended_at': request.form['ended_at'], 'winner': int(request.form['winner'])}},
        upsert=False
      )
      game_data['_id'] = str(game_data['_id'])
      return response_helper.success_response('Success update room', game_data)
    except Exception as err:
      msg = str(err)
      print(msg)
      if err.__cause__ == None:
        msg = f'Cannot find data with id: {id}'
      return response_helper.fail_response(msg)