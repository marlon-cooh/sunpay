from flask import Flask #type: ignore
from flask_sqlalchemy import SQLAlchemy #type: ignore
from flask_migrate import Migrate #type: ignore
from os import getenv

app = Flask(__name__)

# URI path for MySQL database.
SQL_ALCHEMY_DATABASE_URI = getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sun_db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
