#!/usr/bin/python3
"""This is the Review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The Review class that inherits from BaseModel"""
    place_id = ''
    user_id = ''
    text = ''
