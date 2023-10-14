#!/usr/bin/python3
""" Unit tests for review.py file"""


import unittest
from models.base_model import BaseModel
import os
from models import storage
from models.engine.file_storage import FileStorage
from models.review import Review


class TestReview(unittest.TestCase):
    """ Unit tests for review.py file"""
        
    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def test_review(self):
        """ Unit tests for review.py file"""

        self.assertTrue(issubclass(Review, BaseModel))

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests instantiation of Review class."""

        b = Review()
        self.assertEqual(str(type(b)), "<class 'models.review.Review'>")
        self.assertIsInstance(b, Review)
        self.assertTrue(issubclass(type(b), BaseModel))
if __name__ == "__main__":
    unittest.main()
