from __init__ import db
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from flask import current_app

class EditedRecipe(db.Model):
    __tablename__ = 'edited_recipes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    ingredients = db.Column(db.String(256), nullable=False)
    instructions = db.Column(db.String(256), nullable=True)
    image_name = db.Column(db.String(64), nullable=True)
    cleaned_ingredients = db.Column(db.String(256), nullable=True)
    edited_by = db.Column(db.String(128), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, ingredients, instructions, image_name, cleaned_ingredients, edited_by):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.image_name = image_name
        self.cleaned_ingredients = cleaned_ingredients
        self.edited_by = edited_by

    def alldetails(self):
        return {
            "id": self.id,
            "title": self.title,
            "ingredients": self.ingredients,
            "instructions": self.instructions,
            "image_name": self.image_name,
            "cleaned_ingredients": self.cleaned_ingredients,
            "edited_by": self.edited_by,
            "timestamp": self.timestamp
        }

def initEditedRecipes():
    with current_app.app_context():
        print("Creating edited recipe tables")
        db.create_all()
