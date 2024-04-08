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
from flask import Flask, render_template

app = Flask(__name__)

# Other routes and API endpoints

# Route to serve the Vue.js application
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

# Initialize Flask extensions: SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)