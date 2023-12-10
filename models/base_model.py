#!/usr/bin/python3
"""
This python script defines the BaseModel class that is a foundation
for other models within the AirBnB project.
"""

from datetime import datetime
from uuid import uuid4


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
        if kwargs is not None and kwargs != {}:
            for attribute in kwargs:
                if attribute == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif attribute == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[attribute] = kwargs[attribute]
        else:
            from models import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ This method returns a string representation of an instance """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ This method updates the instance attribute updated_at with
        the current datetime """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ This method is the first piece of serialization/deserialization
        process that creates a dictionary represenation of the BaseModel class
        and returns a dictionary with all keys/values of object
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        return obj_dict
