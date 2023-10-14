#!/usr/bin/python3
""" Unit tests for review.py file"""


import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ Unit tests for review.py file"""

    def test_review(self):
        """ Unit tests for review.py file"""

        self.assertTrue(issubclass(Review, BaseModel))


if __name__ == "__main__":
    unittest.main()
