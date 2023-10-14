#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import pycodestyle


class TestBaseModel(unittest.TestCase):

    """Test Cases for the BaseModel class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    # def tearDown(self):
    #     """Tears down test methods."""
    #     self.resetStorage()
    #     pass

    # def resetStorage(self):
    #     """Resets FileStorage data."""
    #     FileStorage._FileStorage__objects = {}
    #     if os.path.isfile(FileStorage._FileStorage__file_path):
    #         os.remove(FileStorage._FileStorage__file_path)

    # def test_init(self):
    #     """
    #     Test the initialization of the BaseModel class.

    #     It checks whether the BaseModel instance is correctly initialized,
    #     including the data types of its attributes.
    #     """
    #     model = BaseModel()
    #     self.assertIsInstance(model.id, str)
    #     self.assertIsInstance(model.created_at, datetime)
    #     self.assertIsInstance(model.updated_at, datetime)

    # def test_base_model_type(self):
    #     """Test if init is ok with with type BaseModel"""

    #     model = BaseModel()
    #     self.assertIsInstance(model, BaseModel)

    # def test_str(self):
    #     """
    #     Test the __str__ method of the BaseModel class.

    #     It checks if the __str__ method returns a string representation
    #     with the expected format.
    #     """
    #     model = BaseModel()
    #     model_str = str(model)
    #     self.assertIn("[BaseModel] ({})".format(model.id), model_str)

    # def test_save(self):
    #     """
    #     Test the save method of the BaseModel class.

    #     It checks if the save method updates the updated_at attribute.
    #     """
    #     model = BaseModel()
    #     old_updated_at = model.updated_at
    #     model.save()
    #     self.assertNotEqual(old_updated_at, model.updated_at)

    # def test_to_dict(self):
    #     """
    #     Test the to_dict method of the BaseModel class.

    #     It checks if the to_dict method returns a dictionary with the
    #     expected keys and values.
    #     """
    #     model = BaseModel()
    #     model_dict = model.to_dict()
    #     self.assertIsInstance(model_dict, dict)
    #     self.assertIn('__class__', model_dict)
    #     self.assertIn('created_at', model_dict)
    #     self.assertIn('updated_at', model_dict)
    #     self.assertEqual(model_dict['__class__'], 'BaseModel')

# class TestPycodestyle(unittest.TestCase):
#     """
#     test that we conform to PEP-8
#     """
#     def test_checking(self):
#         """Testing
#         pycodestyle"""
#         style = pycodestyle.StyleGuide(quit=True)
#         result = style.check_files(['models/base_model.py'])
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
#         boolVal = len(BaseModel.__module__.__doc__) > 1
#         self.assertTrue(boolVal)

#     def test_class_doc(self):
#         """
#         Test if module documentation exists
#         """
#         boolVal = len(BaseModel.__doc__) > 1
#         self.assertTrue(boolVal)

#     def test_init_doc(self):
#         """
#         Test if module documentation exists
#         """
#         boolVal = len(BaseModel.__init__.__doc__) > 1
#         self.assertTrue(boolVal)

#     def test_str_doc(self):
#         """
#         Test if module documentation exists
#         """
#         boolVal = len(BaseModel.__str__.__doc__) > 1
#         self.assertTrue(boolVal)

#     def test_save_doc(self):
#         """
#         Test if module documentation exists
#         """
#         boolVal = len(BaseModel.save.__doc__) > 1
#         self.assertTrue(boolVal)

#     def test_to_dict_doc(self):
#         """
#         Test if module documentation exists
#         """
#         boolVal = len(BaseModel.to_dict.__doc__) > 1
#         self.assertTrue(boolVal)

if __name__ == "__main__":
    unittest.main()
