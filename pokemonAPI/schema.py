"""Marshmallow Schemas."""

from marshmallow import Schema, fields


class PokedexSchema(Schema):
    """Schema for Pokedex Models."""

    name = fields.Str()
    dex_id = fields.Integer()
    picture = fields.Str()
