from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from .helpers.mongo_config import DBCONFIG

lm = LoginManager()
mongoconfig = DBCONFIG().client
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config['SECRET_KEY'] = 'child-track2019'
db = SQLAlchemy(app)
lm.init_app(app)
from .controller import *

