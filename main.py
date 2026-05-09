from flask import Flask, render_template, request, redirect
from data import db_session
from data.models import Recipe, Ingredient
from data.user import User
from forms.user import RegisterForm
from forms.user import LoginForm
from flask_login import login_user, logout_user, login_required
from flask_login import LoginManager, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/recipes.db")

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


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


@app.route('/add_recipes')
def add_recipes():
    return render_template('add_recipes.html')


@app.route('/recipe/<int:id_dish>')
def recipe(id_dish):
    from_page = request.args.get('from_page', 'all')
    db_sess = db_session.create_session()
    recipe = db_sess.query(Recipe).filter(Recipe.id == id_dish).first()
    if recipe:
        res_info = recipe.ingredients_info.split('\n')
        return render_template('recipe_for_dishes.html', recipe=recipe, dish_info=res_info, from_page=from_page)
    return "Рецепт не найден", 404


@app.route('/favourites')
def favourites():
    if current_user.is_authenticated:
        return render_template('favourites.html')
    else:
        return render_template('not_registered_favourites.html')


@app.route('/add_to_favourite/<int:id_to_fav>')
def add_to_favourite(id_to_fav):
    if not current_user.is_authenticated:
        return render_template('not_registered_favourites.html')

    db_sess = db_session.create_session()
    recipe = db_sess.query(Recipe).filter(Recipe.id == id_to_fav).first()
    # не готово
    return redirect('/favourites')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('registration.html', title='Регистрация',
                                   form=form, message='Пароли не совпадают')

        db_sess = db_session.create_session()

        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('registration.html', title='Регистрация',
                                   form=form, message='Такой пользователь уже есть')

        user = User(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data
        )
        user.set_password(form.password.data)

        db_sess.add(user)
        db_sess.commit()

        return redirect('/login')

    return render_template('registration.html', title='Регистрация', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')

        return render_template('authorization.html',
                               message='Неправильный логин или пароль',
                               form=form)
    return render_template('authorization.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
