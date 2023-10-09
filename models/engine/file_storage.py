#!/usr/bin/python3

import json

class FileStorage:
    __file_path = ''
    __objects = {}

    def all(self):
        #returns dic of __objects
        return FileStorage.__objects
    
    def new(self, obj):
        #sets in __objects the obj with key <obj class name>.id
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        #serializes __objects to the JSON file (path: __file_path)
        json.dump(self.__objects, self.__file_path)

    def reload(self):
        #  deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
        #  otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        __object = json.load(self.__file_path)
