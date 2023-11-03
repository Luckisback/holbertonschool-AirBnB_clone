#!/usr/bin/python3
"""Test for Review"""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_attr(self):
        """Test attributes"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_instance(self):
        """Test if it's an instance of Review"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_type_attr(self):
        """Test type attributes"""
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

if __name__ == '__main__':
    unittest.main()
