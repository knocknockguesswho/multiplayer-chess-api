from flask import Flask, request, Response
from bson.objectid import ObjectId
from json import dumps
from pymongo import ReturnDocument
import asyncio
from ...connection import db
from ...helpers import ResponseHelper

response_helper = ResponseHelper()

class UserControllers:
  # GET
  def get_user(self):
    try:
      result = list(db.users.find())
      for user in result:
        user['_id'] = str(user['_id'])
        del user['password']
      if len(result) <= 0:
        result = 'empty'
      return response_helper.success_response('Success get users', result)
    except Exception as err:
      print(err)
      return response_helper.fail_response('Get user failed', 401)
  def get_user_by_id(self, id):
    try:
      result = db.users.find_one({'_id': ObjectId(id)})
      result['_id'] = str(result['_id'])
      del result['password']
      return response_helper.success_response('Success get user by id', result)
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
      result = {
        '_id': id,
        'first_name': update_data['first_name'],
        'last_name': update_data['last_name'],
        'username': update_data['username']
      }
      return response_helper.success_response('Success update user', result)
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