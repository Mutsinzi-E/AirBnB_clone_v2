#!/usr/bin/python3
"""Unittest for the User class."""

import unittest
from os import getenv

from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User."""

    def setUp(self):
        """Set up a User instance."""
        self.user = User()

    def test_is_subclass_of_base_model(self):
        """Test that User inherits from BaseModel."""
        from models.base_model import BaseModel

        self.assertIsInstance(self.user, BaseModel)

    def test_id_exists(self):
        """Test that User has an id."""
        self.assertIsInstance(self.user.id, str)

    def test_email_exists(self):
        """Test that email exists."""
        expected = None if getenv("HBNB_TYPE_STORAGE") == "db" else ""
        self.assertEqual(self.user.email, expected)

    def test_password_exists(self):
        """Test that password exists."""
        expected = None if getenv("HBNB_TYPE_STORAGE") == "db" else ""
        self.assertEqual(self.user.password, expected)

    def test_first_name_exists(self):
        """Test that first_name exists."""
        expected = None if getenv("HBNB_TYPE_STORAGE") == "db" else ""
        self.assertEqual(self.user.first_name, expected)

    def test_last_name_exists(self):
        """Test that last_name exists."""
        expected = None if getenv("HBNB_TYPE_STORAGE") == "db" else ""
        self.assertEqual(self.user.last_name, expected)

    def test_unique_ids(self):
        """Test that different Users have different ids."""
        user2 = User()
        self.assertNotEqual(self.user.id, user2.id)


if __name__ == "__main__":
    unittest.main()
