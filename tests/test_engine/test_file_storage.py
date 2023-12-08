#!/usr/bin/python3
"""Test for FileStorage class"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Unittest for FileStorage"""

    def test_default_file_path(self):
        """Test if the default file path exists"""
        fs = FileStorage()
        self.assertEqual(fs._FileStorage__file_path, "file.json")

    def test_all_method(self):
        """Test the all method"""
        fs = FileStorage()
        all_objects = fs.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_method(self):
        """Test the new method"""
        fs = FileStorage()
        new_model = BaseModel()
        fs.new(new_model)
        self.assertIn(f"{new_model.__class__.__name__}.{new_model.id}", fs.all())

    def test_save_method(self):
        """Test the save method"""
        fs = FileStorage()
        new_model = BaseModel()
        fs.new(new_model)
        fs.save()
        with open(fs._FileStorage__file_path, 'r') as file:
            data = file.read()
            self.assertIn(new_model.id, data)

    def test_reload_method(self):
        """Test the reload method"""
        fs = FileStorage()
        new_model = BaseModel()
        fs.new(new_model)
        fs.save()

        # Creating a new FileStorage instance to simulate reloading
        fs2 = FileStorage()
        fs2.reload()
        loaded_objects = fs2.all()
        self.assertIn(f"{new_model.__class__.__name__}.{new_model.id}", loaded_objects)


if __name__ == '__main__':
    unittest.main()
