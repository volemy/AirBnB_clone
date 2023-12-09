#!/usr/bin/python3
"""This module contains a review clas that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class inherits from the BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
