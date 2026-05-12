from flask_restful import Resource, abort
from flask import jsonify
from data import db_session
from data.models import Recipe


class RecipesResource(Resource):
    def get(self, recipe_id):
        session = db_session.create_session()
        recipe = session.query(Recipe).get(recipe_id)
        if not recipe:
            abort(404, message=f"Recipe {recipe_id} not found")
        return jsonify({'recipe': recipe.to_dict(
            only=('title', 'cooking_time', 'instructions', 'image_file'))})


class RecipesListResource(Resource):
    def get(self):
        session = db_session.create_session()
        recipes = session.query(Recipe).all()
        return jsonify({'recipes': [item.to_dict(
            only=('id', 'title', 'cooking_time')) for item in recipes]})
