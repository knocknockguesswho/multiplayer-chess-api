from flask import Flask
from .routes import routes

def create_app():
  return routes