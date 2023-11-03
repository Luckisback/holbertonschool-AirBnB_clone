#!/usr/bin/python3
"""Test for User"""
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_default_attributes(self):
        """Test the default attributes of a User instance."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attribute_types(self):
        """Test the data types of User attributes."""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

if __name__ == "__main__":
    unittest.main()
