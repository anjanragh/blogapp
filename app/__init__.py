from flask import Flask
from config import Config
# __name__ is the name of the package in which this code is defined i.e 'app'
app = Flask(__name__)
app.config.from_object(Config)
from app import routes
