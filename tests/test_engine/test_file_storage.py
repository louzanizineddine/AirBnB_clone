#!/usr/bin/python3
""" Unit tests for file_storage.py file"""


import os
import models
import unittest
from models import *
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City


class TestFileStorage(unittest.TestCase):
    """test class for file storage"""

    @classmethod
    def setUpClass(mycls):
        """Function that intialize test parameters
        within unittests for testing only"""

        try:
            os.rename("file.json", "mytmp")
        except Exception:
            pass

    @classmethod
    def tearDownClass(mycls):
        """Function that removes test parameters
        that created by setup class
        within unittests for testing only"""

        try:
            os.remove("file.json")
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}

    def test_storage_init(self):
        """ test correct type of class
        """
        self.assertEqual(type(models.storage), FileStorage)

    def test_save_w_arg(self):
        """
        description : test save method with args
        """
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_new_w_none(self):
        """
        description : test new method with none
        as
        """
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_new_w_arg(self):
        """
        description : test new method with args
        """
        # TypeError: new() takes 2 positional
        # arguments but 3 were given
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel, 2)

    def test_reload_w_none(self):
        """
        description : test reload method with
        None as args
        """
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_reload_no_json(self):
        """ test case if no json file exist
        """
        with self.assertRaises(FileNotFoundError):
            models.storage.reload()
            raise FileNotFoundError

    def test_reload(self):
        """ test reload method after
        saving
        """
        rvie = Review()
        models.storage.new(rvie)
        models.storage.save()
        models.storage.reload()
        objcts = FileStorage._FileStorage__objects
        self.assertIn("Review." + rvie.id, objcts)

    def test_file_storage_atributes(self):
        """
        check the attributes of file storage
        """
        json_storage = FileStorage()
        self.assertEqual(json_storage._FileStorage__file_path, "file.json")
        self.assertTrue(isinstance(json_storage._FileStorage__objects, dict))


if __name__ == "__main__":
    unittest.main()
