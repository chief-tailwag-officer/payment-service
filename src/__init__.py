from flask import Flask

from src.config.config import Config
from src.routes import api

app = Flask(__name__)
# Keep the order so common Response properties are always on top
app.json.sort_keys = False

config = Config().dev_config

app.env = config.ENV

app.register_blueprint(api, url_prefix="/api")
