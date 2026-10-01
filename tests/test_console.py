#!/usr/bin/python3
"""Unittest for the HBNB console."""

import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNB command interpreter."""

    def setUp(self):
        """Set up the console."""
        self.console = HBNBCommand()

    def test_quit(self):
        """Test quit command."""
        self.assertTrue(self.console.do_quit(""))

    def test_EOF(self):
        """Test EOF command."""
        self.assertTrue(self.console.do_EOF(""))

    def test_emptyline(self):
        """Test empty line command."""
        self.assertIsNone(self.console.emptyline())

    def test_create_missing_class(self):
        """Test create without a class name."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.do_create("")
            self.assertEqual(
                output.getvalue().strip(),
                "** class name missing **"
            )

    def test_create_invalid_class(self):
        """Test create with an invalid class name."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.do_create("InvalidClass")
            self.assertEqual(
                output.getvalue().strip(),
                "** class doesn't exist **"
            )

    def test_create_with_string_parameter(self):
        """Test create with a quoted string parameter."""
        with patch("console.storage.new") as new:
            with patch("sys.stdout", new=StringIO()) as output:
                self.console.do_create(
                    'State name="New_York"'
                )
                instance = new.call_args[0][0]
                self.assertEqual(instance.name, "New York")
                self.assertTrue(output.getvalue().strip())

    def test_create_with_integer_parameters(self):
        """Test create with integer parameters."""
        with patch("console.storage.new") as new:
            with patch("sys.stdout", new=StringIO()) as output:
                self.console.do_create(
                    "Place number_rooms=4 number_bathrooms=2 "
                    "max_guest=10 price_by_night=300"
                )
                instance = new.call_args[0][0]
                self.assertEqual(instance.number_rooms, 4)
                self.assertEqual(instance.number_bathrooms, 2)
                self.assertEqual(instance.max_guest, 10)
                self.assertEqual(instance.price_by_night, 300)
                self.assertTrue(output.getvalue().strip())

    def test_create_with_float_parameters(self):
        """Test create with float parameters."""
        with patch("console.storage.new") as new:
            with patch("sys.stdout", new=StringIO()) as output:
                self.console.do_create(
                    "Place latitude=37.773972 longitude=-122.431297"
                )
                instance = new.call_args[0][0]
                self.assertEqual(instance.latitude, 37.773972)
                self.assertEqual(instance.longitude, -122.431297)
                self.assertTrue(output.getvalue().strip())

    def test_create_skips_invalid_parameters(self):
        """Test create skips parameters that cannot be recognized."""
        with patch("console.storage.new") as new:
            with patch("sys.stdout", new=StringIO()) as output:
                self.console.do_create(
                    'State name="California" invalid=value '
                    'empty= number_rooms=not_a_number'
                )
                instance = new.call_args[0][0]
                self.assertEqual(instance.name, "California")
                self.assertFalse(hasattr(instance, "invalid"))
                self.assertTrue(output.getvalue().strip())

    def test_show_missing_class(self):
        """Test show without a class name."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.do_show("")
            self.assertEqual(
                output.getvalue().strip(),
                "** class name missing **"
            )

    def test_show_invalid_class(self):
        """Test show with an invalid class name."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.do_show("InvalidClass")
            self.assertEqual(
                output.getvalue().strip(),
                "** class doesn't exist **"
            )

    def test_show_missing_id(self):
        """Test show without an instance id."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.do_show("BaseModel")
            self.assertEqual(
                output.getvalue().strip(),
                "** instance id missing **"
            )

    def test_show_missing_instance(self):
        """Test show with an unknown instance."""
        with patch("console.storage.all", return_value={}):
            with patch("sys.stdout", new=StringIO()) as output:
                self.console.do_show("BaseModel 1234")
                self.assertEqual(
                    output.getvalue().strip(),
                    "** no instance found **"
                )

    def test_destroy_missing_class(self):
        """Test destroy without a class name."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.do_destroy("")
            self.assertEqual(
                output.getvalue().strip(),
                "** class name missing **"
            )

    def test_destroy_invalid_class(self):
        """Test destroy with an invalid class name."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.do_destroy("InvalidClass")
            self.assertEqual(
                output.getvalue().strip(),
                "** class doesn't exist **"
            )

    def test_destroy_missing_id(self):
        """Test destroy without an instance id."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.do_destroy("BaseModel")
            self.assertEqual(
                output.getvalue().strip(),
                "** instance id missing **"
            )

    def test_destroy_missing_instance(self):
        """Test destroy with an unknown instance."""
        with patch("console.storage.all", return_value={}):
            with patch("sys.stdout", new=StringIO()) as output:
                self.console.do_destroy("BaseModel 1234")
                self.assertEqual(
                    output.getvalue().strip(),
                    "** no instance found **"
                )

    def test_all_invalid_class(self):
        """Test all with an invalid class name."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.do_all("InvalidClass")
            self.assertEqual(
                output.getvalue().strip(),
                "** class doesn't exist **"
            )

    def test_update_missing_class(self):
        """Test update without a class name."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.do_update("")
            self.assertEqual(
                output.getvalue().strip(),
                "** class name missing **"
            )

    def test_update_invalid_class(self):
        """Test update with an invalid class name."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.do_update("InvalidClass")
            self.assertEqual(
                output.getvalue().strip(),
                "** class doesn't exist **"
            )

    def test_update_missing_id(self):
        """Test update without an instance id."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.do_update("BaseModel")
            self.assertEqual(
                output.getvalue().strip(),
                "** instance id missing **"
            )

    def test_update_missing_instance(self):
        """Test update with an unknown instance."""
        with patch("console.storage.all", return_value={}):
            with patch("sys.stdout", new=StringIO()) as output:
                self.console.do_update("BaseModel 1234")
                self.assertEqual(
                    output.getvalue().strip(),
                    "** no instance found **"
                )

    def test_update_missing_attribute(self):
        """Test update without an attribute name."""
        with patch("console.storage.all", return_value={
            "BaseModel.1234": object()
        }):
            with patch("sys.stdout", new=StringIO()) as output:
                self.console.do_update("BaseModel 1234")
                self.assertEqual(
                    output.getvalue().strip(),
                    "** attribute name missing **"
                )

    def test_update_missing_value(self):
        """Test update without a value."""
        with patch("console.storage.all", return_value={
            "BaseModel.1234": object()
        }):
            with patch("sys.stdout", new=StringIO()) as output:
                self.console.do_update("BaseModel 1234 name")
                self.assertEqual(
                    output.getvalue().strip(),
                    "** value missing **"
                )


if __name__ == "__main__":
    unittest.main()
