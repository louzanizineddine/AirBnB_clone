#!/usr/bin/python3
""" Unit tests for city.py file"""

import unittest
import os
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ Unit tests for city.py file"""

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
    
    def test_city_class(self):
        """Test if the inheritance works"""

        self.assertTrue(issubclass(City, BaseModel))

    def test_8_instantiation(self):
        """Tests instantiation of City class."""

        c = City()
        self.assertEqual(str(type(c)), "<class 'models.city.City'>")
        self.assertIsInstance(c, City)
        self.assertTrue(issubclass(type(c), BaseModel))

if __name__ == "__main__":
    unittest.main()
