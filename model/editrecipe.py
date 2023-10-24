# Import necessary modules
import csv

# Create a list to hold recipe data
recipes_data = []

# Initialize recipe data (for demonstration purposes)
recipes_data.append({'id': 1, 'title': 'Spaghetti Bolognese', 'recipe': 'Cook pasta and make a rich tomato meat sauce.'})
recipes_data.append({'id': 2, 'title': 'Chicken Stir-Fry', 'recipe': 'Stir-fry chicken and vegetables in a hot wok.'})

# Function to add a new recipe to the data list
def add_recipe(title, recipe):
    new_id = len(recipes_data) + 1
    new_recipe = {'id': new_id, 'title': title, 'recipe': recipe}
    recipes_data.append(new_recipe)
    return new_recipe

# Function to save the recipe data to a CSV file
def save_to_csv():
    file_path = 'api/editedrecipedatabase.csv'
    with open(file_path, mode='w', newline='') as file:
        fieldnames = ['id', 'title', 'recipe']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(recipes_data)

