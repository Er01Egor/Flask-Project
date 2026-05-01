import sqlalchemy
from .db_session import SqlAlchemyBase
import sqlalchemy.orm as orm

recipe_ingredients = sqlalchemy.Table(
    'recipe_ingredients',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('recipe_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('recipe.id')),
    sqlalchemy.Column('ingredient_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('ingredient.id'))
)


class Recipe(SqlAlchemyBase):
    __tablename__ = 'recipe'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String(100), nullable=False)
    image_file = sqlalchemy.Column(sqlalchemy.String(100), default='default.jpg')
    cooking_time = sqlalchemy.Column(sqlalchemy.Integer)
    ingredients_info = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    instructions = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    ingredients = orm.relationship('Ingredient', secondary=recipe_ingredients, backref='recipes')


class Ingredient(SqlAlchemyBase):
    __tablename__ = 'ingredient'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(50), unique=True, nullable=False)
