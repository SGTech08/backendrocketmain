from __init__ import app, db
from flask_login import UserMixin
from sqlalchemy.exc import IntegrityError
import os
import pandas as pd

# Recipe model
class Recipe(db.Model, UserMixin):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    ingredients = db.Column(db.String(256), nullable=False)
    instructions = db.Column(db.String(256), nullable=True)  # Assuming instructions can be nullable
    image_name = db.Column(db.String(64), nullable=True)  # Assuming image_name can be nullable
    cleaned_ingredients = db.Column(db.String(256), nullable=True)  # Assuming cleaned_ingredients can be nullable

    def __init__(self, title, ingredients, instructions, image_name, cleaned_ingredients):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.image_name = image_name
        self.cleaned_ingredients = cleaned_ingredients

    def alldetails(self):
        return {
            "id": self.id,
            "title": self.title,
            "ingredients": self.ingredients,
            "instructions": self.instructions,  # Added instructions
            "image_name": self.image_name,
            "cleaned_ingredients": self.cleaned_ingredients
        }

# Favorite mode
# Function to initialize recipes
def initRecipes():
    with app.app_context():
        print("Creating recipe tables")
        db.create_all()
        if db.session.query(Recipe).count() > 0:
            return

        basedir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(basedir, "../static/data/recipes.csv")  # Changed to use os.path.join for better compatibility
        df = pd.read_csv(file_path)

        for index, row in df.iterrows():
            recipe = Recipe(
                title=row['Title'],
                ingredients=row['Ingredients'],
                instructions=row.get('Instructions', None),  # Added a get method to handle the possibility of the key not existing
                image_name=row.get('Image_Name', None),
                cleaned_ingredients=row.get('Cleaned_Ingredients', None)
            )

            db.session.add(recipe)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                print(f"Duplicate recipe or error: {recipe.title}")
            except Exception as e:
                db.session.rollback()
                print(f"Error adding recipe at index {index}: {str(e)}")

if __name__ == "__main__":
    initRecipes()
