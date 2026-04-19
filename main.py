from flask import Flask, render_template

TITLE = 'Smart Kitchen'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('card_main.html', title=TITLE)


@app.route('/all_recipes')
def all_recipes():
    return render_template('all_recipes.html', title=TITLE)


@app.route('/search_page')
def search_page():
    return render_template('search_page.html', title=TITLE)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
