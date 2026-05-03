from flask import Flask, render_template, request
from data import db_session
from data.models import Recipe, Ingredient
from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/recipes.db")


@app.route('/')
@app.route('/index')
def index():
    return render_template('card_main.html')


@app.route('/all_recipes')
def all_recipes():
    db_sess = db_session.create_session()
    recipes = db_sess.query(Recipe).all()
    return render_template('all_recipes.html', recipes=recipes)


@app.route('/search_page', methods=['GET', 'POST'])
def search_page():
    recipes = []
    gap_product = []
    if request.method == 'POST':
        list_products = request.form.get('ingredients')
        if list_products:
            for line in list_products.split(','):
                product = line.strip().capitalize()
                gap_product.append(product)
        print(gap_product)
    db_sess = db_session.create_session()

    recipes = db_sess.query(Recipe).join(Recipe.ingredients).filter(Ingredient.name.in_(gap_product)).distinct().all()
    return render_template('search_page.html', recipes=recipes)


@app.route('/recipe/<int:id_dish>')
def recipe(id_dish):
    id_dish_list = []
    id_dish_list.append(id_dish)
    print(id_dish_list)

    db_sess = db_session.create_session()
    recipes = db_sess.query(Recipe).join(Recipe.ingredients).filter(Recipe.id.in_(id_dish_list)).distinct().all()
    for elem in recipes:
        res_info = elem.ingredients_info.split('\n')
        return render_template('recipe_for_dishes.html', recipes=recipes, id_dish=id_dish, dish_info=res_info)


@app.route('/register', methods=['GET', 'POST'])
def register():
    pass


@app.route('/login')
def login():
    pass


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
