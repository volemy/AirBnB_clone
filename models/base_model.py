#!/usr/bin/python3
"""
This python script defines the BaseModel class that is a foundation
for other models within the AirBnB project.
"""

from datetime import datetime
from uuid import uuid4

datetime_format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """
    This is the BaseModel class method.
    This class defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        instantiation of the BaseModel class.

        Attributes:
        id (str): Assigns universally unique identification (id) of object
        created_at: assigns current datetime when instance is created
        updated_at:  assigns current datetime when instance is created
        and will be updated everytime you change the object
        """
        if kwargs:
            for attribute_name, value in kwargs.items():
                if attribute_name == 'created_at' or attribute_name == 'updated_at':
                    setattr(self, attribute_name, datetime.strptime(value, datetime_format))
                elif attribute_name != '__class__':
                    setattr(self, attribute_name, value)
        else:

            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ This method returns a string representation of an instance """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ This method updates the instance attribute updated_at with
        the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ This method is the first piece of serialization/deserialization
        process that creates a dictionary represenation of the BaseModel class
        and returns a dictionary with all keys/values of object
        """
        obj_dict = {}
        obj_dict["__class__"] = self.__class__.__name__
        for attribute_name, value in self.__dict__.items():
            if isinstance(value, datetime):
                obj_dict[attribute_name] = value.isoformat()
            else:
                obj_dict[attribute_name] = value
        return obj_dict
