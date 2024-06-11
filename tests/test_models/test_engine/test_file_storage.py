#!/usr/bin/python3
"""Unittest module for the FileStorage class"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json


class TestFileStorage(unittest.TestCase):
    """Unittests for testing FileStorage"""
    def setUp(self):
        """Set up of instances"""
        self.my_storage = FileStorage()
        self.my_model = BaseModel()
        self.my_model_id = self.my_model.__class__.__name__ + '.' +self.my_model.id
        self.file_path = "file.json"

    def tearDown(self):
        """Class method to close test case environment"""
        FileStorage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_FileStorage_all(self):
        """Test for all method"""
        self.assertIsInstance(self.my_storage.all(), dict)

    def test_FileStorage_new(self):
        """Test for new method"""
        self.my_storage.new(self.my_model)
        self.assertIn(self.my_model_id, self.my_storage.all())

    def test_FileStorage_save(self):
        """Test for save method"""
        self.my_storage.new(self.my_model)
        self.my_storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_FileStorage_reload(self):
        """Test for reload method"""
        self.my_storage.new(self.my_model)
        self.my_storage.save()
        self.my_storage._FileStorage__objects.clear()
        self.my_storage.reload()
        self.assertIn(self.my_model_id, self.my_storage.all())


if __name__ == '__main__':
    unittest.main()
