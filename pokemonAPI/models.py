"""Define Database Model Structures."""
from pokemonAPI import db, app
import os


class Pokedex(db.Model):
    """
    Pokemon Model Data.

    Table of all types of pokemon. Pokedex. Limited to one model per species.
    Contains all the specific species info.

    Args:
        name (str): name of pokemonz
        id (int): pokedex id

    Attributes:
        name (str): name of pokemonz
        dex_id (int): pokedex id
        picture (str): path to picture

    """

    __tablename__ = "pokedex"
    name = db.Column(db.String(30))
    dex_id = db.Column(db.Integer, primary_key=True)
    picture = db.Column(db.String(150))
    instances = db.relationship('Pokemon',
                                backref='pokedex',
                                lazy='dynamic')

    def __init__(self, poke_id, name):
        """Constructor Method."""
        self.dex_id = int(poke_id)
        self.name = name
        self.picture = os.path.join(app.config['STATIC_DIR'],
                                    str(poke_id).zfill(3) + ".jpg")


class Pokemon(db.Model):
    """Individual Pokemons.

    Model for actual individual pokemons. I.E, my pikachu vs your pikachu.
    Used primarily to store individual info (nicknames, etc).

    Args:
        species (str): name of Pokemon species
        nickname (str): Optional nickname for Pokemon
        level (int): pokemon level

    Attributes:
        species (Pokemon): link to corresponding Pokemon model
        name (str): nickname, or species name
        level (int): level of pokemon
        moves (int): pokemon moves
    """

    __tablename__ = "pokemon"
    poke_id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.Integer, db.ForeignKey('pokedex.dex_id'))


class Trainer(db.Model):
    """
    Trainer Database Model Data.

    Stuff here.

    Args:
        name (str): name of trainer

    Attributes:
        name (str): name of trainer
    """

    __tablename__ = "trainer"
    name = db.Column(db.String(30), primary_key=True)
    pokemon_caught = db.Column(db.Integer)

    def __init__(self, name):
        """Constructor Method."""
        self.name = name
        self.pokemon_caught = 0
