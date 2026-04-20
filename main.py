from flask import Flask, render_template
from data import db_session
from data.models import Recipe, Ingredient

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
    db_sess.close()
    return render_template('all_recipes.html', recipes=recipes)


@app.route('/search_page')
def search_page():
    return render_template('search_page.html')


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
