#!/usr/bin/python3
"""Unittest for the BaseModel class."""

import unittest
from datetime import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel."""

    def setUp(self):
        """Set up test instances."""
        self.model = BaseModel()

    def test_id_is_string(self):
        """Test that id is a string."""
        self.assertIsInstance(self.model.id, str)

    def test_id_is_unique(self):
        """Test that every instance gets a unique id."""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime."""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime."""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        """Test the string representation."""
        expected = "[BaseModel] ({}) {}".format(
            self.model.id, self.model.__dict__
        )
        self.assertEqual(str(self.model), expected)

    def test_save_updates_updated_at(self):
        """Test that save updates updated_at."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict_returns_dict(self):
        """Test that to_dict returns a dictionary."""
        self.assertIsInstance(self.model.to_dict(), dict)

    def test_to_dict_contains_class(self):
        """Test that to_dict contains the class name."""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")

    def test_to_dict_datetime_are_strings(self):
        """Test that datetime values are converted to strings."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def test_to_dict_custom_attributes(self):
        """Test that custom attributes are included."""
        self.model.name = "My_First_Model"
        self.model.my_number = 89

        model_dict = self.model.to_dict()

        self.assertEqual(model_dict["name"], "My_First_Model")
        self.assertEqual(model_dict["my_number"], 89)


if __name__ == "__main__":
    unittest.main()
