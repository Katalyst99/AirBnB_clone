#!/usr/bin/python3
"""The Unittest module for City"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Unittests for testing City class"""

    my_city = City()

    def test_is_city(self):
        """Test for inheritance"""
        self.assertIsInstance(self.my_city, City)

    def test_city_attributes(self):
        """Test User class atributes"""
        self.assertEqual(self.my_city.state_id, "")
        self.assertEqual(self.my_city.name, "")


if __name__ == '__main__':
    unittest.main()
