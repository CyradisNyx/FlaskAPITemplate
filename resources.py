"""API Resources."""

from flask_restful import Resource


class Trainers(Resource):
    """Users class."""

    def get(self, name):
        """Get user info."""
        return {name: 'lol'}

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

    def post(self, id):
        """Add new task."""
        pass


class PokemonList(Resource):
    """Task list class."""

    def get(self):
        """Get entire list of tasks."""
        return {'get': 'list'}
