#!/usr/bin/python3
"""Unittest for DBStorage."""

import os
import unittest
from datetime import datetime

import MySQLdb

from models import storage
from models.user import User


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") != "db",
    "DBStorage is not active"
)
class TestDBStorage(unittest.TestCase):
    """Test the DBStorage engine."""

    @classmethod
    def setUpClass(cls):
        """Set up the MySQL connection."""
        cls.db = MySQLdb.connect(
            host=os.getenv("HBNB_MYSQL_HOST"),
            user=os.getenv("HBNB_MYSQL_USER"),
            passwd=os.getenv("HBNB_MYSQL_PWD"),
            db=os.getenv("HBNB_MYSQL_DB")
        )

    @classmethod
    def tearDownClass(cls):
        """Close the MySQL connection."""
        cls.db.close()

    def setUp(self):
        """Clean the users table before each test."""
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM users")
        self.db.commit()
        cursor.close()

    def test_storage_is_db_storage(self):
        """Test that the active storage is DBStorage."""
        self.assertEqual(storage.__class__.__name__, "DBStorage")

    def test_new_and_save_inserts_user(self):
        """Test that new and save insert a user into MySQL."""
        user = User(
            email="dbtest@example.com",
            password="password123",
            first_name="Test",
            last_name="User"
        )

        storage.new(user)
        storage.save()

        cursor = self.db.cursor()
        cursor.execute(
            "SELECT id, email, password, first_name, last_name "
            "FROM users WHERE id = %s",
            (user.id,)
        )
        row = cursor.fetchone()
        cursor.close()

        self.assertIsNotNone(row)
        self.assertEqual(row[0], user.id)
        self.assertEqual(row[1], "dbtest@example.com")
        self.assertEqual(row[2], "password123")
        self.assertEqual(row[3], "Test")
        self.assertEqual(row[4], "User")

    def test_all_returns_saved_user(self):
        """Test that all returns a saved user."""
        user = User(
            email="alltest@example.com",
            password="password123"
        )

        storage.new(user)
        storage.save()

        objects = storage.all(User)

        key = "User.{}".format(user.id)

        self.assertIn(key, objects)
        self.assertEqual(objects[key].id, user.id)
        self.assertEqual(objects[key].email, user.email)

    def test_delete_removes_user_from_database(self):
        """Test that delete removes a user from MySQL."""
        user = User(
            email="deletetest@example.com",
            password="password123"
        )

        storage.new(user)
        storage.save()

        storage.delete(user)
        storage.save()

        cursor = self.db.cursor()
        cursor.execute(
            "SELECT id FROM users WHERE id = %s",
            (user.id,)
        )
        row = cursor.fetchone()
        cursor.close()

        self.assertIsNone(row)

    def test_user_datetime_columns(self):
        """Test that created_at and updated_at are stored."""
        user = User(
            email="datetest@example.com",
            password="password123"
        )

        storage.new(user)
        storage.save()

        cursor = self.db.cursor()
        cursor.execute(
            "SELECT created_at, updated_at FROM users WHERE id = %s",
            (user.id,)
        )
        row = cursor.fetchone()
        cursor.close()

        self.assertIsNotNone(row)
        self.assertIsInstance(row[0], datetime)
        self.assertIsInstance(row[1], datetime)

    def test_close(self):
        """Test that close removes the current session."""
        storage.close()
        self.assertIsNotNone(storage._DBStorage__session)

        storage.reload()
        self.assertIsNotNone(storage._DBStorage__session)


if __name__ == "__main__":
    unittest.main()
