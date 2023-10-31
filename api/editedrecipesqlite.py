from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'  # SQLite database file named recipes.db
db = SQLAlchemy(app)
api = Api(app)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    ingredients = db.Column(db.String(256), nullable=False)
    instructions = db.Column(db.String(256), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "ingredients": self.ingredients,
            "instructions": self.instructions
        }

class RecipeListResource(Resource):
    def get(self):
        recipes = Recipe.query.all()
        return jsonify([recipe.serialize() for recipe in recipes])
    
    def post(self):
        data = request.get_json()
        new_recipe = Recipe(title=data['title'], ingredients=data['ingredients'], instructions=data['instructions'])
        db.session.add(new_recipe)
        db.session.commit()
        return jsonify(new_recipe.serialize())

class RecipeResource(Resource):
    def delete(self, recipe_id):
        recipe = Recipe.query.get_or_404(recipe_id)
        db.session.delete(recipe)
        db.session.commit()
        return '', 204

api.add_resource(RecipeListResource, '/recipes')
api.add_resource(RecipeResource, '/recipes/<int:recipe_id>')

if __name__ == '__main__':
    db.create_all()  # Creates the database tables defined by the model before running the app
    app.run(debug=True)  # Running the Flask application
