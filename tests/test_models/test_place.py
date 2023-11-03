#!/usr/bin/python3
""" Test for place """
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
        self.assertEqual(place.amenity_ids, [])
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

    def test_name(self):
        """Test the name attribute"""
        place = Place()
        place.name = "San Francisco"
        self.assertEqual(place.name, "San Francisco")

    def test_description(self):
        """Test the description attribute"""
        place = Place()
        place.description = "La maison de Julien Barbier"
        self.assertEqual(place.description, "La maison de Julien Barbier")

    def test_number_rooms(self):
        """Test the number_rooms attribute"""
        place = Place()
        place.number_rooms = 6
        self.assertEqual(place.number_rooms, 6)

    def test_bathrooms(self):
        """Test the number_bathrooms attribute"""
        place = Place()
        place.number_bathrooms = 3
        self.assertEqual(place.number_bathrooms, 3)

    def test_max_guest(self):
        """Test the max_guest attribute"""
        place = Place()
        place.max_guest = 18
        self.assertEqual(place.max_guest, 18)

    def test_price_by_night(self):
        """Test the price_by_night attribute"""
        place = Place()
        place.price_by_night = 300
        self.assertEqual(place.price_by_night, 300)

    def test_latitude(self):
        """Test the latitude attribute"""
        place = Place()
        place.latitude = 37.77750
        self.assertEqual(place.latitude, 37.77750)

    def test_longitude(self):
        """Test the longitude attribute"""
        place = Place()
        place.longitude = -122.41639
        self.assertEqual(place.longitude, -122.41639)

    def test_amenity_ids(self):
        """Test the amenity_ids attribute"""
        place = Place()
        place.amenity_ids = ["Computer", "Wifi", "Coffee Machine"]
        self.assertEqual(place.amenity_ids, ["Computer", "Wifi", "Coffee Machine"])

    def test_city_id_relation(self):
        """Test the relationship between Place and City"""
        place = Place()
        city = City()
        place.city_id = city.id
        self.assertEqual(place.city_id, city.id)

    def test_user_id_relation(self):
        """Test the relationship between Place and User"""
        place = Place()
        user = User()
        place.user_id = user.id
        self.assertEqual(place.user_id, user.id)

if __name__ == '__main__':
    unittest.main()

