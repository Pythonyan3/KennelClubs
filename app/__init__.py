from app.config import Configuration
from flask import Flask
from .main import main_blueprint as main

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(main, url_prefix='')
