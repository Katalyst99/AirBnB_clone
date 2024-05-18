#!/usr/bin/python3
"""This is the User module"""
from models.base_model import BaseModel


class User(BaseModel):
    """The User class that inherits from BaseModel"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
