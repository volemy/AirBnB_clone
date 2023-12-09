#!/usr/bin/python3
"""Unittest for place class"""

import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):
    """Unittest for place class"""

    def test_default_attributes(self):
        """Test default attributes"""
        new_place = Place()
        self.assertEqual(new_place.city_id, "")
        self.assertEqual(new_place.user_id, "")
        self.assertEqual(new_place.name, "")
        self.assertEqual(new_place.description, "")
        self.assertEqual(new_place.number_rooms, 0)
        self.assertEqual(new_place.number_bathrooms, 0)
        self.assertEqual(new_place.max_guest, 0)
        self.assertEqual(new_place.price_by_night, 0)
        self.assertEqual(new_place.latitude, 0.0)
        self.assertEqual(new_place.longitude, 0.0)
        self.assertEqual(new_place.amenity_ids, [])

    def test_place_attributes(self):
        """Test place attributes"""
        new_place = Place()
        new_place.city_id = "NY"
        new_place.user_id = "123e4567-e89b-12d3-a456-426614174000"
        new_place.name = "New York"
        new_place.description = "A city in the United States"
        new_place.number_rooms = 5
        new_place.number_bathrooms = 2
        new_place.max_guest = 10
        new_place.price_by_night = 100
        new_place.latitude = 40.7128
        new_place.longitude = -74.0060
        new_place.amenity_ids = ["123e4567-e89b-12d3-a456-426614174000",
                                 "123e4567-e89b-12d3-a456-426614174001"]

        self.assertEqual(new_place.city_id, "NY")
        self.assertEqual(new_place.user_id,
                         "123e4567-e89b-12d3-a456-426614174000")
        self.assertEqual(new_place.name, "New York")
        self.assertEqual(new_place.description, "A city in the United States")
        self.assertEqual(new_place.number_rooms, 5)
        self.assertEqual(new_place.number_bathrooms, 2)
        self.assertEqual(new_place.max_guest, 10)
        self.assertEqual(new_place.price_by_night, 100)
        self.assertEqual(new_place.latitude, 40.7128)
        self.assertEqual(new_place.longitude, -74.0060)
        self.assertEqual(new_place.amenity_ids, [
            "123e4567-e89b-12d3-a456-426614174000",
            "123e4567-e89b-12d3-a456-426614174001"
        ])

    def test_place_to_dict(self):
        """Test for to_dict method"""
        new_place = Place()
        new_place.name = "New York"
        new_place.my_number = 89
        new_place_dict = new_place.to_dict()
        self.assertEqual(new_place_dict['__class__'], 'Place')
        self.assertEqual(new_place_dict['name'], 'New York')
        self.assertEqual(new_place_dict['my_number'], 89)
        self.assertEqual(type(new_place_dict['created_at']), str)
        self.assertEqual(type(new_place_dict['updated_at']), str)

    def test_place_init_with_dict(self):
        """Test initialization with dictionary representation"""
        sample_dict = {
            'id': '123e4567-e89b-12d3-a456-426614174000',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-02T12:00:00.000000',
            'name': 'New York',
            'my_number': 89
        }

        new_place = Place(**sample_dict)
        self.assertEqual(new_place.id, '123e4567-e89b-12d3-a456-426614174000')
        self.assertEqual(type(new_place.created_at), datetime)
        self.assertEqual(type(new_place.updated_at), datetime)
        self.assertEqual(new_place.name, 'New York')
        self.assertEqual(new_place.my_number, 89)


if __name__ == '__main__':
    unittest.main()
