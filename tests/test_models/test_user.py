#!/usr/bin/python3
"""The Unittest module for User"""
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Unittests for testing User class"""

    my_user = User()

    def test_is_user(self):
        """Test for inheritance"""
        self.assertIsInstance(self.my_user, User)

    def test_user_attributes(self):
        """Test User class atributes"""
        self.assertEqual(self.my_user.email, "")
        self.assertEqual(self.my_user.password, "")
        self.assertEqual(self.my_user.first_name, "")
        self.assertEqual(self.my_user.last_name, "")


if __name__ == '__main__':
    unittest.main()
