from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes

# Define your recipe generator function here
def generate_recipe(ingredients):
    # Your existing code for generating a recipe prompt
    ingredients_list = ingredients.split(",")
    recipe_prompt = "Write a recipe based on the ingredients provided here:\n"
    recipe_prompt += "Ingredients:\n"
    for ingredient in ingredients_list:
        recipe_prompt += f"- {ingredient.strip()}\n"
    return recipe_prompt

# Define a route for generating a recipe
@app.route('/generate_recipe', methods=['POST'])
def generate_recipe_route():
    data = request.get_json()
    ingredients = data.get('ingredients', '')
    recipe_prompt = generate_recipe(ingredients)
    return jsonify(recipe_prompt)

if __name__ == '__main__':
    app.run(debug=True)
