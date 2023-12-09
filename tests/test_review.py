#!/usr/bin/python3
"""Unittest for Review"""

import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage


class TestReview(unittest.TestCase):
    """Unittest for Review"""

    def test_default_attributes(self):
        """Test default attributes"""
        new_review = Review()
        self.assertEqual(new_review.place_id, "")
        self.assertEqual(new_review.user_id, "")
        self.assertEqual(new_review.text, "")

    def test_review_attributes(self):
        """Test review attributes"""
        new_review = Review()
        new_review.place_id = "NY"
        new_review.user_id = "123e4567-e89b-12d3-a456-426614174000"
        new_review.text = "A city in the United States"
        self.assertEqual(new_review.place_id, "NY")
        self.assertEqual(new_review.user_id,
                         "123e4567-e89b-12d3-a456-426614174000")
        self.assertEqual(new_review.text, "A city in the United States")

    def test_review_init_with_dict(self):
        """Test initialization with dictionary representation"""
        sample_dict = {
            'id': '123e4567-e89b-12d3-a456-426614174000',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-02T12:00:00.000000',
            'place_id': 'NY',
            'user_id': '123e4567-e89b-12d3-a456-426614174000',
            'text': 'A city in the United States'
        }

        new_review = Review(**sample_dict)
        self.assertEqual(new_review.id, '123e4567-e89b-12d3-a456-426614174000')
        self.assertEqual(type(new_review.created_at), datetime)
        self.assertEqual(type(new_review.updated_at), datetime)
        self.assertEqual(new_review.place_id, 'NY')
        self.assertEqual(new_review.user_id,
                         '123e4567-e89b-12d3-a456-426614174000')
        self.assertEqual(new_review.text, 'A city in the United States')


if __name__ == '__main__':
    unittest.main()
