#!/usr/bin/python3
"""Unittest for the Place class."""

import unittest

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
        self.assertEqual(self.place.city_id, "")

    def test_user_id(self):
        """Test user_id."""
        self.assertEqual(self.place.user_id, "")

    def test_name(self):
        """Test name."""
        self.assertEqual(self.place.name, "")

    def test_description(self):
        """Test description."""
        self.assertEqual(self.place.description, "")

    def test_number_rooms(self):
        """Test number_rooms."""
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms(self):
        """Test number_bathrooms."""
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest(self):
        """Test max_guest."""
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night(self):
        """Test price_by_night."""
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude(self):
        """Test latitude."""
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude(self):
        """Test longitude."""
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids(self):
        """Test amenity_ids."""
        self.assertEqual(self.place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
