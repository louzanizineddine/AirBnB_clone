#!/usr/bin/python3
""" Class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances """
import json


class FileStorage:
    """a class serialization-deserialization"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """ sets in _objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to JSON file"""
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            dic = {}
            for key in self.__objects:
                dic[key] = self.__objects[key].to_dict()
            file.write(json.dumps(dic))

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
