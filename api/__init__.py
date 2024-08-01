from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.config.Config')
db = SQLAlchemy(app)

from api import routes, models