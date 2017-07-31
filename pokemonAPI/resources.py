"""API Resources."""

from flask_restful import Resource, abort, reqparse
from pokemonAPI import db, models


class Trainers(Resource):
    """Users class."""

    def get(self, name):
        """Get user info."""
        temp = models.Trainer.query.get(name)
        if temp is None:
            abort(404)
        else:
            return {name: temp.pokemon_caught}

    def post(self, name):
        """Add new user."""
        pass

    def put(self, name):
        """Update existing user."""
        pass

    def delete(self, name):
        """Delete user."""
        pass


class Pokemon(Resource):
    """Tasks class."""

    def get(self, id):
        """Get individual tasks info."""
        pass


class PokemonList(Resource):
    """Task list class."""

    def get(self):
        """Get entire list of tasks."""
        return {'get': 'list'}
