#!/usr/bin/python3
"""Unittest for the Place class."""

import unittest
from os import getenv

from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for Place."""

    def setUp(self):
        """Set up a Place instance."""
        self.place = Place()

    def test_is_subclass_of_base_model(self):
        """Test that Place inherits from BaseModel."""
        self.assertIsInstance(self.place, BaseModel)

    def test_id_exists(self):
        """Test that Place has an id."""
        self.assertIsInstance(self.place.id, str)

    def test_city_id(self):
        """Test city_id."""
        expected = None if getenv("HBNB_TYPE_STORAGE") == "db" else ""
        self.assertEqual(self.place.city_id, expected)

    def test_user_id(self):
        """Test user_id."""
        expected = None if getenv("HBNB_TYPE_STORAGE") == "db" else ""
        self.assertEqual(self.place.user_id, expected)

    def test_name(self):
        """Test name."""
        expected = None if getenv("HBNB_TYPE_STORAGE") == "db" else ""
        self.assertEqual(self.place.name, expected)

    def test_description(self):
        """Test description."""
        expected = None if getenv("HBNB_TYPE_STORAGE") == "db" else ""
        self.assertEqual(self.place.description, expected)

    def test_number_rooms(self):
        """Test number_rooms."""
        expected = None if getenv("HBNB_TYPE_STORAGE") == "db" else 0
        self.assertEqual(self.place.number_rooms, expected)

    def test_number_bathrooms(self):
        """Test number_bathrooms."""
        expected = None if getenv("HBNB_TYPE_STORAGE") == "db" else 0
        self.assertEqual(self.place.number_bathrooms, expected)

    def test_max_guest(self):
        """Test max_guest."""
        expected = None if getenv("HBNB_TYPE_STORAGE") == "db" else 0
        self.assertEqual(self.place.max_guest, expected)

    def test_price_by_night(self):
        """Test price_by_night."""
        expected = None if getenv("HBNB_TYPE_STORAGE") == "db" else 0
        self.assertEqual(self.place.price_by_night, expected)

    def test_latitude(self):
        """Test latitude."""
        expected = None if getenv("HBNB_TYPE_STORAGE") == "db" else 0.0
        self.assertEqual(self.place.latitude, expected)

    def test_longitude(self):
        """Test longitude."""
        expected = None if getenv("HBNB_TYPE_STORAGE") == "db" else 0.0
        self.assertEqual(self.place.longitude, expected)

    def test_amenity_ids(self):
        """Test amenity_ids."""
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertFalse(hasattr(self.place, "amenity_ids"))
        else:
            self.assertEqual(self.place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
