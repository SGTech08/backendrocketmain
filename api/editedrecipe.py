from flask import Blueprint, jsonify, request
from model.editrecipe import recipes_data, add_recipe, save_to_csv

# Create a Blueprint for the edited recipe API
edited_recipe_api = Blueprint('edited_recipe_api', __name__, url_prefix='/api/edited_recipe')

@edited_recipe_api.route('/recipes', methods=['GET'])
def get_recipes():
    return jsonify(recipes_data)

@edited_recipe_api.route('/add_recipe', methods=['POST'])
def create_recipe():
    data = request.get_json()
    title = data.get('title')
    recipe = data.get('recipe')

    if title and recipe:
        new_recipe = add_recipe(title, recipe)
        save_to_csv()  # Save the updated data to the CSV file
        return jsonify(new_recipe), 201
    else:
        return jsonify({"error": "Both title and recipe are required"}), 400
