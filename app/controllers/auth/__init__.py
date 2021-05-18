from bson.objectid import ObjectId
from flask import Flask, request
from flask_bcrypt import Bcrypt
import jwt
import datetime
from ...connection import db
from ...helpers import ResponseHelper
from ...config import config

auth = Flask(__name__)
bcrypt = Bcrypt(auth)
response_helper = ResponseHelper()
auth.config['SECRET_KEY'] = config['SECRET_KEY']

class AuthController:
  # POST
  def sign_up(self):
    try:
      pw_hash = bcrypt.generate_password_hash(request.form['password'], rounds=10)
      user_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'username': request.form['username'],
        'password': pw_hash,
        'avatar': '', # source image url
        'rank_point': 0,
        'friend_list': [], # assign with list of friends user_detail['_id'] { friend_id: ObjectId }
        'game_history': [], # assign with list of game_history_id { room_id: ObjectId }
        'isLogin': False
      }
      db.users.insert_one(user_data)
      user_data['_id'] = str(user_data['_id'])
      del user_data['password']
      return response_helper.success_response('Sign up success', user_data)
    except Exception as err:
      print(err)
      return response_helper.fail_response(str(err), 401)

  def sign_in(self):
    try:
      user_data = {
        'username': request.form['username'],
        'password': request.form['password']
      }
      result = db.users.find_one({'username': user_data['username']})
      pw_match = bcrypt.check_password_hash(result['password'], user_data['password'])
      token = jwt.encode(
        {
          'user': user_data['username'],
          'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, auth.config['SECRET_KEY']
      )
      if pw_match:
        db.users.find_one_and_update(
          {'username': user_data['username']},
          {'$set': {'isLogin': True}},
          upsert=False
        )
        return response_helper.success_response('Sign in success', {'token': token.decode('utf-8')})
      else:
        raise Exception("Sorry username or password invalid")
    except Exception as err:
      msg = str(err)
      print(err)
      return response_helper.fail_response(msg, 401)

  def sign_out(self, id):
    try:
      db.users.find_one_and_update(
        {'_id': ObjectId(id)},
        {'$set': {'isLogin': False}},
        upsert=False
      )
      return response_helper.success_response('Sign out success')
    except Exception as err:
      msg = str(err)
      print(err)
      return response_helper.fail_response(msg, 401)