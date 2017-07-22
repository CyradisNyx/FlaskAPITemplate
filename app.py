"""Main File."""
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from resources import Pokemon, PokemonList, Trainers

# APP SETUP
app = Flask(__name__)
app.config.from_pyfile('config.py')

# DATABASE SETUP
db = SQLAlchemy(app)

# API SETUP
api = Api(app)
api.add_resource(Pokemon, '/api/pokemon/<int:id>')
api.add_resource(PokemonList, '/api/pokemon')
api.add_resource(Trainers, '/api/trainer/<string:name>')

if __name__ == '__main__':
    app.run()
