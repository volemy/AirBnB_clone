#!/usr/bin/python3
"""Unittest for BaseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Unittest for BaseModel"""

    def test_id(self):
        """Test for id"""
        my_model = BaseModel()
        self.assertEqual(type(my_model.id), str)

    def test_created_at(self):
        """Test for created_at"""
        my_model = BaseModel()
        self.assertEqual(type(my_model.created_at), datetime)

    def test_updated_at(self):
        """Test for updated_at"""
        my_model = BaseModel()
        self.assertEqual(type(my_model.updated_at), datetime)

    def test_str(self):
        """Test for __str__"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        string = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(string, str(my_model))

    def test_save(self):
        """Test for save"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_to_dict(self):
        """Test for to_dict"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertEqual(my_model_dict['name'], 'My First Model')
        self.assertEqual(my_model_dict['my_number'], 89)
        self.assertEqual(type(my_model_dict['created_at']), str)
        self.assertEqual(type(my_model_dict['updated_at']), str)

    def test_uuid(self):
        """Test for uuid"""
        my_model = BaseModel()
        uuid1 = my_model.id
        my_model = BaseModel()
        uuid2 = my_model.id
        self.assertNotEqual(uuid1, uuid2)
