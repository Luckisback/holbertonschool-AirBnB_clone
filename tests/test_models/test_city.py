#!/usr/bin/python3
"""Unittest for city class"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """testing the correct functioning of the class"""
    def test_attr(self):
        """test attributes"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_id(self):
        "Test id"
        city = City()
        self.assertEqual(str, type(city.id))
