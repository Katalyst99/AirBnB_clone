#!/usr/bin/python3
"""The Unittest module for Amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittests for testing Amenity class"""

    my_amenity = Amenity()

    def test_is_amenity(self):
        """Test for inheritance"""
        self.assertIsInstance(self.my_amenity, Amenity)

    def test_amenity_attributes(self):
        """Test amenity class atributes"""
        self.assertEqual(self.my_amenity.name, "")


if __name__ == '__main__':
    unittest.main()
