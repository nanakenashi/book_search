import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.config import choise_config

environment = os.getenv('FLASK_ENV', 'development')

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(choise_config(environment))
app.config.from_pyfile('config.cfg', silent=True)
db = SQLAlchemy(app)

import src.views
