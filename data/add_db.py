from data import db_session
from data.models import Recipe, Ingredient


def add_database():
    db_session.global_init("../db/recipes.db")
    db_sess = db_session.create_session()

    recipe1 = Recipe(
        id=1,
        title="Борщ",
        image_file="1.jpg",
        instruction="""
            1. Нашинкуйте овощи
            2. Сварите бульон
            3. dcdds
            4. wewds
        """,
        cooking_time=90
    )
    db_sess.add(recipe1)

    ingredient1 = Ingredient(id=1, name="Свекла")
    ingredient2 = Ingredient(id=2, name="Капуста")
    ingredient3 = Ingredient(id=3, name="Картофель")
    ingredient4 = Ingredient(id=4, name="Мясо")
    ingredient5 = Ingredient(id=5, name="Лук")
    ingredient6 = Ingredient(id=6, name="Морковь")
    ingredient7 = Ingredient(id=7, name="Томатная паста")
    ingredient8 = Ingredient(id=8, name="Чеснок")
    ingredient9 = Ingredient(id=9, name="Уксус")
    ingredient10 = Ingredient(id=10, name="Зелень")

    recipe1.ingredients.append(ingredient1)
    recipe1.ingredients.append(ingredient2)
    recipe1.ingredients.append(ingredient3)
    recipe1.ingredients.append(ingredient4)
    recipe1.ingredients.append(ingredient5)
    recipe1.ingredients.append(ingredient6)
    recipe1.ingredients.append(ingredient7)
    recipe1.ingredients.append(ingredient8)
    recipe1.ingredients.append(ingredient9)
    recipe1.ingredients.append(ingredient10)

    db_sess.add(ingredient1)
    db_sess.add(ingredient2)
    db_sess.add(ingredient3)
    db_sess.add(ingredient4)
    db_sess.add(ingredient5)
    db_sess.add(ingredient6)
    db_sess.add(ingredient7)
    db_sess.add(ingredient8)
    db_sess.add(ingredient9)
    db_sess.add(ingredient10)

    db_sess.commit()
    print("База данных успешно заполнена!")


if __name__ == '__main__':
    add_database()
