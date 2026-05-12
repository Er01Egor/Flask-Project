import sqlalchemy
from .db_session import SqlAlchemyBase
import sqlalchemy.orm as orm
from sqlalchemy_serializer import SerializerMixin


class Ingredient(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'ingredients'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(50), unique=True, nullable=False)


class Recipe(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'recipes'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String(100), nullable=False)
    image_file = sqlalchemy.Column(sqlalchemy.String(100), default='default.jpg')
    cooking_time = sqlalchemy.Column(sqlalchemy.Integer)
    ingredients_info = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    instructions = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    # ingredients = orm.relationship('Ingredient', secondary=recipe_ingredients, backref='recipes')


recipe_ingredients = sqlalchemy.Table(
    'recipe_ingredients',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('recipe_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('recipes.id')),
    sqlalchemy.Column('ingredient_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('ingredients.id'))
)

favorites_table = sqlalchemy.Table(
    'favorites',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('user_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column('recipe_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('recipes.id'))
)

Recipe.ingredients = orm.relationship('Ingredient', secondary=recipe_ingredients, backref='recipes')
