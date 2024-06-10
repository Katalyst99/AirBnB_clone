#!/usr/bin/python3
"""The Unittest module for Review"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Unittests for testing Review class"""

    my_review = Review()

    def test_is_review(self):
        """Test for inheritance"""
        self.assertIsInstance(self.my_review, Review)

    def test_review_attributes(self):
        """Test Review class atributes"""
        self.assertEqual(self.my_review.place_id, "")
        self.assertEqual(self.my_review.user_id, "")
        self.assertEqual(self.my_review.text, "")


if __name__ == '__main__':
    unittest.main()
