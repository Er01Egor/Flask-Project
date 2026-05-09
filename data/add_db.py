from data import db_session
from data.models import Recipe, Ingredient
from data.dish_values import recipes_list
import os

folder_db = '../db'
if not os.path.exists(folder_db):
    os.makedirs(folder_db)
else:
    print(f'Папка {folder_db} уже существует')

bb = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(bb, "..", "db", "recipes.db")


def add_database():
    db_session.global_init(db_path)
    db_sess = db_session.create_session()

    db_sess.query(Recipe).delete()
    db_sess.query(Ingredient).delete()
    db_sess.commit()
    for data in recipes_list:
        recipe = Recipe(
            title=data["title"],
            image_file=data["image"],
            cooking_time=data["time"],
            ingredients_info=data["ingredients_info"],
            instructions=data["instructions"]
        )
        db_sess.add(recipe)
        for ing_name in data["ingredients"]:
            ingredient = db_sess.query(Ingredient).filter(Ingredient.name == ing_name).first()

            if not ingredient:
                ingredient = Ingredient(name=ing_name)

            recipe.ingredients.append(ingredient)

        db_sess.add(recipe)

    db_sess.commit()
    print(f"БД заполнен, блюда: {len(recipes_list)}")


if __name__ == '__main__':
    add_database()
