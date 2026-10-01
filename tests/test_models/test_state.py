#!/usr/bin/python3
"""Unittest for the State class."""

import unittest
from os import getenv

from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State."""

    def setUp(self):
        """Set up a State instance."""
        self.state = State()

    def test_is_subclass_of_base_model(self):
        """Test that State inherits from BaseModel."""
        self.assertIsInstance(self.state, BaseModel)

    def test_id_exists(self):
        """Test that State has an id."""
        self.assertIsInstance(self.state.id, str)

    def test_name(self):
        """Test that name exists."""
        expected = None if getenv("HBNB_TYPE_STORAGE") == "db" else ""
        self.assertEqual(self.state.name, expected)


if __name__ == "__main__":
    unittest.main()
