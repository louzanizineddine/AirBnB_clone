#!/usr/bin/python3

import json
import os

class FileStorage:
    __file_path = "file.json"
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
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dic = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dic, f)

    def reload(self):
        #  deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
        #  otherwise, do nothing. If the file doesn’t exist, no exception should be raised)

        if os.path.isfile(FileStorage.__file_path) is False:
            pass

        else:
            with open(FileStorage.__filepath, "r", encoding="utf-8") as f:
                FileStorage.__object = json.load(FileStorage.__file_path)
