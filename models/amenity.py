#!/usr/bin/python3
"""Defining classes of Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an Amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""

