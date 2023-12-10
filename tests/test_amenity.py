#!/usr/bin/python3
"""Unittest for Amenity"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Unittest for Amenity"""

    def test_default_attributes(self):
        """Test for default attributes"""
        new_amenity = Amenity()
        self.assertEqual(new_amenity.name, "")

    def test_amenity_attributes(self):
        """Test for user attributes"""
        new_amenity = Amenity()
        new_amenity.name = "Test Amenity"
        self.assertEqual(new_amenity.name, "Test Amenity")

    def test_amenity_instance(self):
        """Test for user instance"""
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_amenity_str(self):
        """Test for __str__ method"""
        new_amenity = Amenity()
        new_amenity.name = "Test Amenity"
        string = "[Amenity] ({}) {}".format(
                new_amenity.id, new_amenity.__dict__)
        self.assertEqual(string, str(new_amenity))

    def test_amenity_save(self):
        """Test for save method"""
        new_amenity = Amenity()
        new_amenity.name = "Test Amenity"
        new_amenity.save()
        self.assertNotEqual(new_amenity.created_at, new_amenity.updated_at)

    def test_amenity_to_dict(self):
        """Test for to_dict method"""
        new_amenity = Amenity()
        new_amenity.name = "Test Amenity"
        new_amenity_dict = new_amenity.to_dict()
        self.assertEqual(new_amenity_dict['__class__'], 'Amenity')
        self.assertEqual(new_amenity_dict['name'], 'Test Amenity')
        self.assertEqual(type(new_amenity_dict['created_at']), str)
        self.assertEqual(type(new_amenity_dict['updated_at']), str)

    def test_amenity_init_with_dict(self):
        """Test initialization with dictionary representation"""
        sample_dict = {
            'id': '123e4567-e89b-12d3-a456-426614174000',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-02T12:00:00.000000',
            'name': 'Test Amenity'
        }

        new_amenity = Amenity(**sample_dict)
        self.assertEqual(new_amenity.id,
                         '123e4567-e89b-12d3-a456-426614174000')
        self.assertEqual(type(new_amenity.created_at), datetime)
        self.assertEqual(type(new_amenity.updated_at), datetime)
        self.assertEqual(new_amenity.name, 'Test Amenity')


if __name__ == '__main__':
    unittest.main()
