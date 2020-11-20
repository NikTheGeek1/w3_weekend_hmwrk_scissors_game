from flask import Flask

app = Flask(__name__)

from app.controllers import controller_welcome
from app.controllers import controller_about
from app.controllers import controller_game