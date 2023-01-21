import os
from flask import Flask
from flask_migrate import Migrate
from .models import db
from .routes import api
from .config import config

app = Flask(__name__)

# Set Environment Variables
env = os.environ.get("ENV", "dev")
app.config.from_object(config[env]) 

# Register SQLAlchemy 
db.init_app(app)

# Register Blueprint
app.register_blueprint(api) 

Migrate(app, db)
