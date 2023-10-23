from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///editedrecipes.db'  # Use your preferred database URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define and initialize other components (routes, models, etc.) as needed

if __name__ == "__main__":
    app.run(debug=True)
