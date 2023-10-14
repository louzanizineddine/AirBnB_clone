#!/usr/bin/python3
""" Unit tests for city.py file"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ Unit tests for city.py file"""

    def test_city_class(self):
        """Test if the inheritance works"""

        self.assertTrue(issubclass(City, BaseModel))


if __name__ == "__main__":
    unittest.main()
