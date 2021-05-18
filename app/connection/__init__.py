from flask_pymongo import MongoClient
from ..config import config

try:
  mongo = MongoClient(
    host=config['DB_HOST'], #db host
    port=int(config['DB_PORT']), #db port
    serverSelectionTimeoutMS=1000
  )
  db = mongo[config['DB_NAME']] #db_name
  mongo.server_info()
  print('Connected to DB')
except Exception as err:
  print("ERROR - Cannot connect to DB")
  print(err)