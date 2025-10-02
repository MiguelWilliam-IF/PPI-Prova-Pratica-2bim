from flask import Flask
from flask_wtf import CSRFProtect
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy()
csrf = CSRFProtect(app)
migrate = Migrate()

db.init_app(app)
migrate.init_app(app, db)

from app import routes, models

with app.app_context():
    db.create_all()