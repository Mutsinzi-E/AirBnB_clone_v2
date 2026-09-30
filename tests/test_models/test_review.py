#!/usr/bin/python3
"""Unittest for the Review class."""

import unittest

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review."""

    def setUp(self):
        """Set up a Review instance."""
        self.review = Review()

    def test_is_subclass_of_base_model(self):
        """Test that Review inherits from BaseModel."""
        self.assertIsInstance(self.review, BaseModel)

    def test_id_exists(self):
        """Test that Review has an id."""
        self.assertIsInstance(self.review.id, str)

    def test_place_id(self):
        """Test place_id."""
        self.assertEqual(self.review.place_id, "")

    def test_user_id(self):
        """Test user_id."""
        self.assertEqual(self.review.user_id, "")

    def test_text(self):
        """Test text."""
        self.assertEqual(self.review.text, "")


if __name__ == "__main__":
    unittest.main()
