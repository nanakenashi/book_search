from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('src.config')
app.config.from_pyfile('config.cfg', silent=True)
db = SQLAlchemy(app)

import src.views
