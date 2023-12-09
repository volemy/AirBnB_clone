#!/usr/bin/python3
"""This module contains a class that inherits from the BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """ This city class inherits from BaseModel """
    state_id = ""
    name = ""
