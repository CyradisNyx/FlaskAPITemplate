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
        evolution (bool): whether or not this pokemon can evolve
        next_evolution (str): name of next evolution
        instances (

    """

    __tablename__ = "pokedex"
    __bind_key__ = "dex"
    dex_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    picture = db.Column(db.String(150))
    evolution = db.Column(db.Boolean)
    next_evolution = db.Column(db.String(30))
    instances = db.relationship('Pokemon',
                                backref='species',
                                lazy='dynamic')

    def __init__(self, poke_id, name):
        """Constructor Method."""
        self.dex_id = int(poke_id)
        self.name = name
        self.picture = os.path.join(app.config['STATIC_DIR'],
                                    str(poke_id).zfill(3) + ".jpg")


class Moves(db.Model):
    """Database of PokeMoves.

    Model for all possible pokemon moves. Static in DEX database, has
    base values for move power/accuracy, which are then modified in use by
    instance Pokemon modifiers.

    Args:
        pass

    Attributes:
        pass
    """

    __tablename__ = "moves"
    __bind_key__ = "dex"
    move_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))


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
        strength (int): strength modifier
        agility (int): agility modifier
        moves (PokeMove): relationship to PokeMove table, where moves are
                          stored
    """

    __tablename__ = "pokemon"
    __bind_key__ = None
    poke_id = db.Column(db.Integer, primary_key=True)
    dex_id = db.Column(db.Integer, db.ForeignKey('pokedex.dex_id'))
    level = db.Column(db.Integer)
    strength = db.Column(db.Integer)
    agility = db.Column(db.Integer)


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
    __bind_key__ = None
    trainer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    pokemon_caught = db.Column(db.Integer)

    def __init__(self, name):
        """Constructor Method."""
        self.name = name
        self.pokemon_caught = 0


class PokeMove(db.Model):
    """
    Model to store moves assigned to individual pokemon.

    Table of individual pokemons moves.

    Args:
        pass

    Attributes:
        pokemove_id (int): id lookup
        
    """

    __tablename__ = "pokemove"
    __bind_key__ = None
    pokemove_id = db.Column(db.Integer, primary_key=True)
