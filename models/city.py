#!/usr/bin/python3
""" class City that inherits from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ a class for cities"""

    state_id = ""
    name = ""
