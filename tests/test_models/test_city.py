#!/usr/bin/python3
"""Test for City"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_instance_creation(self):
        """Test if a City instance can be created."""
        city = City()
        self.assertIsInstance(city, City)

    def test_default_name(self):
        """Test if the default city name is an empty string."""
        city = City()
        self.assertEqual("", city.name)

    def test_id_type(self):
        """Test if the type of city's ID is a string."""
        city = City()
        self.assertEqual(str, type(city.id))

    def test_default_state_id(self):
        """Test if the default state_id is an empty string."""
        city = City()
        self.assertEqual("", city.state_id)

if __name__ == '__main__':
    unittest.main()
