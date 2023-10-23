from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource
from __init__ import db
from .editedrecipe import EditedRecipe

edited_recipe_api = Blueprint('edited_recipe', __name__, url_prefix='/api/editedrecipe')
api = Api(edited_recipe_api)

class EditedRecipes:
    class _getEditedRecipes(Resource):
        def get(self):
            edited_recipes = db.session.query(EditedRecipe).all()
            return jsonify([recipe.alldetails() for recipe in edited_recipes])

    class _getEditedRecipeDetails(Resource):
        def get(self):
            recipe_id = int(request.args.get("id"))
            recipe = db.session.query(EditedRecipe).filter(EditedRecipe.id == recipe_id).first()
            return jsonify(recipe.alldetails())

    class _addEditedRecipe(Resource):
        def post(self):
            data = request.get_json()
            new_recipe = EditedRecipe(
                title=data.get("title"),
                ingredients=data.get("ingredients"),
                instructions=data.get("instructions"),
                image_name=data.get("image_name"),
                cleaned_ingredients=data.get("cleaned_ingredients"),
                edited_by=data.get("edited_by")
            )
            db.session.add(new_recipe)
            db.session.commit()
            return jsonify({"message": "Recipe added successfully"})

api.add_resource(EditedRecipes._getEditedRecipes, "/recipes")
api.add_resource(EditedRecipes._getEditedRecipeDetails, "/recipedetails")
api.add_resource(EditedRecipes._addEditedRecipe, "/addrecipe")
