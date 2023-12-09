#!/usr/bin/python3
"""Unittest for State"""

import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage


class TestState(unittest.TestCase):
    """Unittest for State"""

    def test_default_attributes(self):
        """Test default attributes"""
        new_state = State()
        self.assertEqual(new_state.name, "")
        self.assertIsInstance(new_state.created_at, datetime)
        self.assertIsInstance(new_state.updated_at, datetime)
        self.assertIsInstance(new_state.id, str)

    def test_state_init_with_dict(self):
        """Test initialization with dictionary representation"""
        sample_dict = {
            'id': '123e4567-e89b-12d3-a456-426614174000',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-02T12:00:00.000000',
            'name': 'New York'
        }

        new_state = State(**sample_dict)

        self.assertEqual(new_state.id, '123e4567-e89b-12d3-a456-426614174000')
        self.assertEqual(type(new_state.created_at), datetime)
        self.assertEqual(type(new_state.updated_at), datetime)
        self.assertEqual(new_state.name, 'New York')

    def test_state_attributes(self):
        """Test state attributes"""
        new_state = State()
        new_state.name = "New York"
        self.assertEqual(new_state.name, "New York")

    def test_state_to_dict(self):
        """Test for to_dict method"""
        new_state = State()
        new_state.name = "New York"
        new_state.my_number = 89
        new_state_dict = new_state.to_dict()
        self.assertEqual(new_state_dict['__class__'], 'State')
        self.assertEqual(new_state_dict['name'], 'New York')
        self.assertEqual(new_state_dict['my_number'], 89)
        self.assertEqual(type(new_state_dict['created_at']), str)
        self.assertEqual(type(new_state_dict['updated_at']), str)


if __name__ == '__main__':
    unittest.main()
