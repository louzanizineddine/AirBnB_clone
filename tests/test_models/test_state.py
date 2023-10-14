#!/usr/bin/python3
""" Unit tests for state.py file"""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ Unit tests for state.py file"""

    def test_state(self):
        """Test if the inheritance works"""

        self.assertTrue(issubclass(State, BaseModel))


if __name__ == "__main__":
    unittest.main()
