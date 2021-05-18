from flask import request
from bson.objectid import ObjectId
from json import dumps
from pymongo import ReturnDocument
from ...connection import db
from ...helpers import ResponseHelper

response_helper = ResponseHelper()

class UserController:
  # GET
  def get_user(self):
    try:
      user_data = list(db.users.find())
      for user in user_data:
        user['created_at'] = str(user['_id'].generation_time)
        user['_id'] = str(user['_id'])
        del user['password']
      if len(user_data) <= 0:
        user_data = 'empty'
      return response_helper.success_response('Success get users', user_data)
    except Exception as err:
      print(err)
      return response_helper.fail_response('Get user failed', 401)
  def get_user_by_id(self, id):
    try:
      user_data = db.users.find_one({'_id': ObjectId(id)})
      user_data['_id'] = str(user_data['_id'])
      del user_data['password']
      return response_helper.success_response('Success get user by id', user_data)
    except Exception as err:
      msg = str(err)
      print(err)
      if err.__cause__ == None:
        msg = f'Cannot find data with id: {id}'
      return response_helper.fail_response(msg, 500)

  # PUT
  def update_user(self, id):
    try:
      update_data = db.users.find_one_and_update(
        {'_id': ObjectId(id)},
        {'$set': request.form.to_dict()},
        upsert=False,
        return_document=ReturnDocument.AFTER
      )
      return response_helper.success_response('Success update user', update_data)
    except Exception as err:
      msg = str(err)
      print(err)
      if err.__cause__ == None:
        msg = f'Cannot find data with id: {id}'
      return response_helper.fail_response(msg, 500)

  # DELETE
  def delete_user(self, id):
    try:
      db.users.delete_one({'_id': ObjectId(id)})
      return response_helper.success_response(f'Success delete user with id: {id}')
    except Exception as err:
      print(err)
      return response_helper.fail_response(str(err), 500)