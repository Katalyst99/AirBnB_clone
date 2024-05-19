#!/usr/bin/python3
"""Unittest module for the BaseModel class"""
import unittest
from models.base_model import BaseModel
import datetime

class TestBaseModel(unittest.TestCase):
    """Unittests for testing BaseModel class"""
    def setUp(self):
        self.my_model = BaseModel()

    def testBasemodel_attributes(self):
        """Test of class attributes"""
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        
        self.assertTrue(hasattr(self.my_model, "name"))
        self.assertEqual(self.my_model.name, "My First Model")
        self.assertTrue(hasattr(self.my_model, "my_number"))
        self.assertTrue(hasattr(self.my_model, "id"))
        self.assertTrue(hasattr(self.my_model, "created_at"))

        my_model_json = self.my_model.to_dict()

        self.assertEqual(self.my_model.id,my_model_json['id'])
        self.assertEqual(self.my_model.name,my_model_json['name'])
        self.assertEqual(self.my_model.__class__.__name__, "BaseModel")
        self.assertEqual(self.my_model.my_number,my_model_json['my_number'])

    def test_save_method(self):
        """Test of class save method"""
        self.my_model.save()
        self.assertTrue(hasattr(self.my_model, "updated_at"))
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

    def test_to_dict_method(self):
        """Test to_dict method"""
        my_model_json = self.my_model.to_dict()
        self.assertIsInstance(my_model_json['updated_at'], str)
        self.assertIsInstance(my_model_json['created_at'], str)

if __name__ == '__main__':
    unittest.main()
