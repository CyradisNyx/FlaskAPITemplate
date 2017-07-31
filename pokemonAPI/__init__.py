"""Main File."""
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import pokemonAPI.resources as resources

# APP SETUP
app = Flask(__name__)
app.config.from_object('config')

# DATABASE SETUP
db = SQLAlchemy(app)

# API SETUP
api = Api(app)
api.add_resource(resources.Pokemon, '/api/pokemon/<int:id>')
api.add_resource(resources.PokemonList, '/api/pokemon')
api.add_resource(resources.Trainers, '/api/trainer/<string:name>')

import pokemonAPI.models
