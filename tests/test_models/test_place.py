#!/usr/bin/python3
"""Test for Place"""
import unittest
from models.place import Place
from models.city import City
from models.user import User

class TestPlace(unittest.TestCase):
    def test_instance_creation(self):
        """Test the creation of a Place instance and its attributes"""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, []
        self.assertTrue(isinstance(place.city_id, str))
        self.assertTrue(isinstance(place.user_id, str))
        self.assertTrue(isinstance(place.name, str))
        self.assertTrue(isinstance(place.description, str))
        self.assertTrue(isinstance(place.number_rooms, int))
        self.assertTrue(isinstance(place.number_bathrooms, int))
        self.assertTrue(isinstance(place.max_guest, int))
        self.assertTrue(isinstance(place.price_by_night, int))
        self.assertTrue(isinstance(place.latitude, float))
        self.assertTrue(isinstance(place.longitude, float))
        self.assertTrue(isinstance(place.amenity_ids, list))

    def test_city_id(self):
        """Test the city_id attribute"""
        place = Place()
        place.city_id = "42"
        self.assertEqual(place.city_id, "42")

    def test_user_id(self):
        """Test the user_id attribute"""
        place = Place()
        place.user_id = "0626839210"
        self.assertEqual(place.user_id, "0626839210")

    if __name__ == '__main__':
    unittest.main()
