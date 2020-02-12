import os
basedir = os.path.abspath(os.path.dirname(__file__))


if os.environ.get('DATABASE_URL') is None:
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'child-track.db')

else:
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

if os.environ.get('MONGODB_URI') is None:
	MONGODB_URI = 'mongodb+srv://developerprince:WqkpTkjRkjdOJfAq@cluster0-o0c1g.mongodb.net/child_track'
else:
	MONGODB_URI = os.environ.get('MONGODB_URI')

SECRET_KEY = 'thechild-track2019#'

CSRF_ENABLED = True

class Config(object):
	SECRET_KEY = 'thedeveloperprincepro2019#'
	CSRF_ENABLED = True

class Development(Config):
	DEVELOPMENT = True
	DEBUG = True

class Staging(Config):
	DEVELOPMENT = True
	DEBUG = True

class Testing(Config):
	TESTING = True

class Production(Config):
	DEBUG = False
