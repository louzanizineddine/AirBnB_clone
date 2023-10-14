#!/usr/bin/python3
""" Unit tests for user.py file"""


import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """ Unit tests for user.py file"""

    def test_user(self):
        """Test if the inheritance works"""

        self.assertTrue(issubclass(User, BaseModel))


if __name__ == "__main__":
    unittest.main()
