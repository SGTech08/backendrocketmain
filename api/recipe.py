from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, request, Resource # used for REST API building
import requests  # used for testing
import random
from __init__ import login_manager, app, db
from model.recipes import Recipe

recipe_api = Blueprint('recipe', __name__, url_prefix='/api/recipe')
# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1


api = Api(recipe_api)
class recipes:
    class _getRecipes(Resource):
        def get(self):
            recipes = db.session.query(Recipe).all()
            return jsonify([recipe.alldetails() for recipe in recipes])
        
    class _getrecipedetails(Resource):
        def get(self):
            recipe = db.session.query(Recipe).filter(Recipe.id == int(request.args.get("id"))).first()
            return jsonify(recipe.alldetails())
    
    api.add_resource(_getRecipes, "/recipes")
    api.add_resource(_getrecipedetails, "/recipedetails")