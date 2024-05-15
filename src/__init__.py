import os

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from src.config.config import Config

# loading environment variables
load_dotenv()

app = Flask(__name__)

config = Config().dev_config

app.env = config.ENV
# Keep the order so common Response properties are always on top
app.json.sort_keys = False

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "SQLALCHEMY_DATABASE_URI_DEV")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.environ.get(
    "SQLALCHEMY_TRACK_MODIFICATIONS")


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)

migrate = Migrate(app, db)
from src.domain.user import User

# Register Routes
from src.routes import api

app.register_blueprint(api, url_prefix="/api")
