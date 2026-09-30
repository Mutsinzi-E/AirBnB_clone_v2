#!/usr/bin/python3
"""Unittest for the FileStorage class."""

import os
import unittest

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage."""

    def setUp(self):
        """Set up the test environment."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Clean up the test environment."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_storage_is_file_storage(self):
        """Test that storage is a FileStorage instance."""
        self.assertIsInstance(storage, FileStorage)

    def test_all_returns_dict(self):
        """Test that all returns a dictionary."""
        self.assertIsInstance(storage.all(), dict)

    def test_new_adds_object(self):
        """Test that new adds an object."""
        model = BaseModel()
        key = "BaseModel.{}".format(model.id)

        self.assertIn(key, storage.all())
        self.assertIs(storage.all()[key], model)

    def test_save_creates_file(self):
        """Test that save creates file.json."""
        model = BaseModel()
        storage.save()

        self.assertTrue(os.path.exists("file.json"))

    def test_reload_restores_objects(self):
        """Test that reload restores saved objects."""
        model = BaseModel()
        model.save()

        object_id = model.id

        FileStorage._FileStorage__objects = {}
        storage.reload()

        key = "BaseModel.{}".format(object_id)

        self.assertIn(key, storage.all())
        self.assertIsInstance(storage.all()[key], BaseModel)
        self.assertEqual(storage.all()[key].id, object_id)


if __name__ == "__main__":
    unittest.main()
