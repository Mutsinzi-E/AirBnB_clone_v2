#!/usr/bin/python3
"""Unittest for the FileStorage class."""

import os
import unittest
from os import getenv

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


@unittest.skipIf(
    getenv("HBNB_TYPE_STORAGE") == "db",
    "DBStorage is active"
)
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

    def test_all_returns_internal_objects(self):
        """Test that all returns the internal objects dictionary."""
        self.assertIs(storage.all(), FileStorage._FileStorage__objects)

    def test_new_with_different_models(self):
        """Test that new stores different model types."""
        from models.user import User
        from models.place import Place

        user = User()
        place = Place()

        storage.new(user)
        storage.new(place)

        self.assertIn("User.{}".format(user.id), storage.all())
        self.assertIn("Place.{}".format(place.id), storage.all())

    def test_save_serializes_object(self):
        """Test that save writes the object's dictionary to file.json."""
        import json

        model = BaseModel()
        storage.save()

        with open("file.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        key = "BaseModel.{}".format(model.id)

        self.assertIn(key, data)
        self.assertEqual(data[key]["id"], model.id)
        self.assertEqual(data[key]["__class__"], "BaseModel")

    def test_reload_missing_file(self):
        """Test that reload does nothing when file.json is missing."""
        model = BaseModel()

        if os.path.exists("file.json"):
            os.remove("file.json")

        FileStorage._FileStorage__objects = {}
        storage.reload()

        self.assertNotIn(
            "BaseModel.{}".format(model.id),
            storage.all()
        )

    def test_reload_restores_correct_class(self):
        """Test that reload restores the original model class."""
        from models.user import User

        model = User()
        model.first_name = "Enock"
        model.save()

        object_id = model.id

        FileStorage._FileStorage__objects = {}
        storage.reload()

        key = "User.{}".format(object_id)

        self.assertIn(key, storage.all())
        self.assertIsInstance(storage.all()[key], User)
        self.assertEqual(storage.all()[key].first_name, "Enock")


if __name__ == "__main__":
    unittest.main()
