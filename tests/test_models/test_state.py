#!/usr/bin/python3
"""The Unittest module for State"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Unittests for testing State class"""

    my_state = State()

    def test_is_state(self):
        """Test for inheritance"""
        self.assertIsInstance(self.my_state, State)

    def test_state_attributes(self):
        """Test State class atributes"""
        self.assertEqual(self.my_state.name, "")


if __name__ == '__main__':
    unittest.main()
