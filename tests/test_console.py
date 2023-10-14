#!/usr/bin/python3
"""Unittests for console.py"""

import unittest
from console import HBNBCommand


class TestHBNB(unittest.TestCase):
    """class to test console.py prompting"""

    def test_prompt_string(self):
        """test the basic prompting"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)
