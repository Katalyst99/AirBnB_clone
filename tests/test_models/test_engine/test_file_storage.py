#!/usr/bin/python3
"""Unittest module for the FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Unittests for testing FileStorage"""
    def setUp(self):
        """Set up of instances"""
        self.my_storage = FileStorage()
        self.my_model = BaseModel()
        self.my_model_id = my_model.__class__.name__ + '.' + self.my_model.id

    def tearDown(self):
        """Class method to close test case environment"""
        FileStorage._FileStorage__objects = {}

    def test_FileStorage_all(self):
        """Test for all method"""
        self.assertIsInstance(self.my_storage.all(), dict)

    def test_FileStorage_new(self):
        """Test for new method"""
        self.storage.new(self.my_model)
        self.assertIn(self.my_model_id, self.my_storage.all())
    def test_FileStorage_save(self):
        """Test for save method"""


if __name__ == '__main__':
    unittest.main()
