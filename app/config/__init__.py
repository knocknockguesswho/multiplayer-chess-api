import os

config = {
  'SECRET_KEY': os.getenv('SECRET_KEY'),
  'DB_HOST': os.getenv('DB_HOST'),
  'DB_PORT': os.getenv('DB_PORT'),
  'DB_NAME': os.getenv('DB_NAME')
}