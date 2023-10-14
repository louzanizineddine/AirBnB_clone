#!/usr/bin/python3
""" Unit tests for user.py file"""


import unittest
from models.base_model import BaseModel
import os
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User
import pycodestyle


class TestUser(unittest.TestCase):
    """ Unit tests for user.py file"""

    # def setUp(self):
    #     """Sets up test methods."""
    #     pass

#     def tearDown(self):
#         """Tears down test methods."""
#         self.resetStorage()
#         pass

#     def test_user(self):
#         """Test if the inheritance works"""

#         self.assertTrue(issubclass(User, BaseModel))


#     def resetStorage(self):
#         """Resets FileStorage data."""
#         FileStorage._FileStorage__objects = {}
#         if os.path.isfile(FileStorage._FileStorage__file_path):
#             os.remove(FileStorage._FileStorage__file_path)

#     def test_instantiation(self):
#         """Tests instantiation of User class."""

#         b = User()
#         self.assertEqual(str(type(b)), "<class 'models.user.User'>")
#         self.assertIsInstance(b, User)
#         self.assertTrue(issubclass(type(b), BaseModel))


# class TestPycodestyle(unittest.TestCase):
#     """
#     test that we conform to PEP-8
#     """
#     def test_checking(self):
#         """Testing
#         pycodestyle"""
#         style = pycodestyle.StyleGuide(quit=True)
#         result = style.check_files(['models/user.py'])
#         self.assertEqual(result.total_errors, 0,
#                          "Found code style errors (and warnings).")


# class TestDocuemntationOfAll(unittest.TestCase):
#     """
#     This class will have the unittesting of that the
#     whole module is well documented
#     """
#     def test_module_doc(self):
#         """
#         Test if module documentation exists
#         """
#         boolVal = len(User.__module__.__doc__) > 1
#         self.assertTrue(boolVal)

#     def test_class_doc(self):
#         """
#         Test if module documentation exists
#         """
#         boolVal = len(User.__doc__) > 1
#         self.assertTrue(boolVal)

#     def test_init_doc(self):
#         """
#         Test if module documentation exists
#         """
#         boolVal = len(User.__init__.__doc__) > 1
#         self.assertTrue(boolVal)

#     def test_str_doc(self):
#         """
#         Test if module documentation exists
#         """
#         boolVal = len(User.__str__.__doc__) > 1
#         self.assertTrue(boolVal)

#     def test_save_doc(self):
#         """
#         Test if module documentation exists
#         """
#         boolVal = len(User.save.__doc__) > 1
#         self.assertTrue(boolVal)

#     def test_to_dict_doc(self):
#         """
#         Test if module documentation exists
#         """
#         boolVal = len(User.to_dict.__doc__) > 1
#         self.assertTrue(boolVal)


if __name__ == "__main__":
    unittest.main()
