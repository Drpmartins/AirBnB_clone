#!/usr/bin/python3
"""Definning the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that Inherits From BaseModels"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
