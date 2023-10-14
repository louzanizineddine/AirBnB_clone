#!/usr/bin/python3
""" Unit tests for amenity.py file"""


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Unit tests for amenity.py file"""
    
    def setUp(self):
        """Sets up test methods."""
        pass

    # def test_amenity(self):
    #     """Test if the inheritance works"""

    #     self.assertTrue(issubclass(Amenity, BaseModel))


if __name__ == "__main__":
    unittest.main()
