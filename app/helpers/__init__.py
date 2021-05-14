from flask import Response
from json import dumps
# from werkzeug.security import safe_str_cmp
# import jwt

class ResponseHelper:
  def success_response(self, message, result=None):
    res = {
      'success': True,
      'message': message
    }
    if result:
      res['data'] = result
    return Response(
      response=dumps(res),
      status=200,
      mimetype='application/json'
    )
  def fail_response(self, message, status=500):
    return Response(
      response=dumps({
        'success': False,
        'message': message
      }),
      status=status,
      mimetype='application/json'
    )
# class JWTHelper:
#   def authenticate(username, password):
#     if 