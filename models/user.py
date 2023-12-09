#!/usr/bin/python3
"""This module contains a class user that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """This user class inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
