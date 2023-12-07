#!/usr/bin/python3
"""
This filestorage class serializes instances to a JSON format.
"""

import json
from models.base_model import BaseModel

class FileStorage():
    """This class serializes instances to a JSON  format"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ This method returns the dictionary of all objects """
        return self.__objects

    def new(self, obj):
        """ This method adds a new object to the __objects dictionary """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        This method serializes __objects to the JSON file
        """
        new_serialized_obj = {}
        for key, obj in self.__objects.items():
            new_serialized_obj[key] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(new_serialized_obj, f)

    def reload(self):
        """ This method deserialize the JSON file to __objects if file
        exists """
        try:
            with open(self.__file_path, "r") as f:
                info = json.load(f)
                for key, value in info.items():
                    class_name, obj_id = key.split('.')
                    obj = globals()[class_name](**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
