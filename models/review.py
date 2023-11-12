#!/usr/bin/python3
"""Definning the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a Review class from Basemodels."""

    place_id = ""
    user_id = ""
    text = ""
