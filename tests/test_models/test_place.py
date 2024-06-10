#!/usr/bin/python3
"""The Unittest module for Place"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Unittests for testing Place class"""

    my_place = Place()

    def test_is_place(self):
        """Test for inheritance"""
        self.assertIsInstance(self.my_place, Place)

    def test_place_attributes(self):
        """Test Place class atributes"""
        self.assertEqual(self.my_place.name, "")
        self.assertEqual(self.my_place.description, "")
        self.assertEqual(self.my_place.city_id, "")
        self.assertEqual(self.my_place.user_id, "")
        self.assertEqual(self.my_place.number_rooms, 0)
        self.assertEqual(self.my_place.number_bathrooms, 0)
        self.assertEqual(self.my_place.max_guest, 0)
        self.assertEqual(self.my_place.price_by_night, 0)
        self.assertEqual(self.my_place.latitude, 0)
        self.assertEqual(self.my_place.longitude, 0)
        self.assertEqual(self.my_place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
