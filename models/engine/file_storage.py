#!/usr/bin/python3
"""Module for FileStorage class."""
import json


class FileStorage:
    """Class for serializtion and deserialization of base classes."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dic of __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Class for serializtion and deserialization of base classes."""

        serialized_objects = {}

        """Iterate through the objects in FileStorage.__objects"""
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

            with open(self.__file_path, "w", encoding="utf-8") as f:
                json.dump(serialized_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        cls = {'BaseModel': BaseModel, "User": User, "Place": Place,
               "Amenity": Amenity, "City": City,
               "Review": Review, "State": State}
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                objs = json.loads(file.read())
                for key in objs:
                    name = objs[key]['__class__']
                    self.__objects[key] = cls[name](**objs[key])
        except FileNotFoundError:
            ...
