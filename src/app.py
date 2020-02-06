from flask import Flask
from .config import app_config
from .models import db, bcrypt

def create_app(env_name):
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])

  db.init_app(app)

  bcrypt.init_app(app)

  @app.route('/')
  def index():
    return 'Congratulations! Your first endpoint is workin'

  return app
