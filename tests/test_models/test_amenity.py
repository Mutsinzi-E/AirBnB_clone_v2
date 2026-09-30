#!/usr/bin/python3
"""Unittest for the Amenity class."""

import unittest

from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity."""

    def setUp(self):
        """Set up an Amenity instance."""
        self.amenity = Amenity()

    def test_is_subclass_of_base_model(self):
        """Test that Amenity inherits from BaseModel."""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_id_exists(self):
        """Test that Amenity has an id."""
        self.assertIsInstance(self.amenity.id, str)

    def test_name(self):
        """Test that name exists."""
        self.assertEqual(self.amenity.name, "")


if __name__ == "__main__":
    unittest.main()
