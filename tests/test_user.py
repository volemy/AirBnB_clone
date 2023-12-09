#!/usr/bin/python3
"""Unittest for User class"""

import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """Unittest for User class"""

    def test_default_attributes(self):
        """Test for default attributes"""
        new_user = User()
        self.assertEqual(new_user.email, "")
        self.assertEqual(new_user.password, "")
        self.assertEqual(new_user.first_name, "")
        self.assertEqual(new_user.last_name, "")

    def test_user_attributes(self):
        """Test for user attributes"""
        new_user = User()
        new_user.email = "test@example.com"
        new_user.password = "password123"
        new_user.first_name = "John"
        new_user.last_name = "Doe"

        self.assertEqual(new_user.email, "test@example.com")
        self.assertEqual(new_user.password, "password123")
        self.assertEqual(new_user.first_name, "John")
        self.assertEqual(new_user.last_name, "Doe")

    def test_user_instance(self):
        """Test for user instance"""
        new_user = User()
        self.assertIsInstance(new_user, User)
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_str(self):
        """Test User __str__ method"""
        user_data = {
            'id': '12345',
            'email': 'test@example.com',
            'password': 'securepwd',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        new_user = User(**user_data)
        expected_str = "[User] ({}) {}".format(new_user.id, new_user.__dict__)
        self.assertEqual(str(new_user), expected_str)

    def test_user_save(self):
        """Test User save method"""
        new_user = User()
        old_updated_at = new_user.updated_at
        new_user.save()
        self.assertNotEqual(old_updated_at, new_user.updated_at)


if __name__ == '__main__':
    unittest.main()
