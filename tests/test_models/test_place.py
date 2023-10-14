#!/usr/bin/python3
""" Unit tests for place.py file"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Unit tests for place.py file"""

    def test_place(self):
        """Test if the inheritance works"""

        self.assertTrue(issubclass(Place, BaseModel))


if __name__ == "__main__":
    unittest.main()
