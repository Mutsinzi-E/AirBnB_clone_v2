#!/usr/bin/python3
"""Unittest for the City class."""

import unittest
from os import getenv

from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City."""

    def setUp(self):
        """Set up a City instance."""
        self.city = City()

    def test_is_subclass_of_base_model(self):
        """Test that City inherits from BaseModel."""
        self.assertIsInstance(self.city, BaseModel)

    def test_id_exists(self):
        """Test that City has an id."""
        self.assertIsInstance(self.city.id, str)

    def test_state_id(self):
        """Test state_id."""
        expected = None if getenv("HBNB_TYPE_STORAGE") == "db" else ""
        self.assertEqual(self.city.state_id, expected)

    def test_name(self):
        """Test name."""
        expected = None if getenv("HBNB_TYPE_STORAGE") == "db" else ""
        self.assertEqual(self.city.name, expected)


if __name__ == "__main__":
    unittest.main()
