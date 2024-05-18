#!/usr/bin/python3
"""This is the City module"""
from models.base_model import BaseModel


class City(BaseModel):
    """The City class that inherits from BaseModel"""
    state_id = ''
    name = ''
