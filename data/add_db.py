from data import db_session
from data.models import Recipe, Ingredient
from data.dish_values import recipes_list


def add_database():
    db_session.global_init("../db/recipes.db")
    db_sess = db_session.create_session()

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
