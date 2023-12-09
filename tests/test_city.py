#!/usr/bin/python3
"""Unittest for City"""

import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """Unittest for City"""

    def test_default_attributes(self):
        """Test default attributes"""
        new_city = City()
        self.assertEqual(new_city.state_id, "")
        self.assertEqual(new_city.name, "")
        self.assertIsInstance(new_city.created_at, datetime)
        self.assertIsInstance(new_city.updated_at, datetime)
        self.assertIsInstance(new_city.id, str)

    def test_city_attributes(self):
        """Test city attributes"""
        new_city = City()
        new_city.state_id = "NY"
        new_city.name = "New York"
        self.assertEqual(new_city.state_id, "NY")
        self.assertEqual(new_city.name, "New York")

    def test_city_init(self):
        """Test for City initialization"""
        new_city = City()
        self.assertEqual(type(new_city), City)

    def test_city_str(self):
        """Test for __str__ method"""
        new_city = City()
        string = "[City] ({}) {}".format(new_city.id, new_city.__dict__)
        self.assertEqual(string, str(new_city))

    def test_city_save(self):
        """Test for save method"""
        new_city = City()
        new_city.save()
        self.assertNotEqual(new_city.created_at, new_city.updated_at)

    def test_city_to_dict(self):
        """Test for to_dict method"""
        new_city = City()
        new_city.name = "New York"
        new_city.my_number = 89
        new_city_dict = new_city.to_dict()
        self.assertEqual(new_city_dict['__class__'], 'City')
        self.assertEqual(new_city_dict['name'], 'New York')
        self.assertEqual(new_city_dict['my_number'], 89)
        self.assertEqual(type(new_city_dict['created_at']), str)
        self.assertEqual(type(new_city_dict['updated_at']), str)


if __name__ == '__main__':
    unittest.main()
