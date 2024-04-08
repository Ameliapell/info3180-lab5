from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
# Add other necessary configurations

# Initialize Flask extensions: SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)