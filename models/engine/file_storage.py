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
        serialized_objects = {}

        # Iterate through the objects in FileStorage.__objects
        for key, obj in FileStorage.__objects.items():
            # Serialize each object using its "to_dict" method and store it in the dictionary
            serialized_objects[key] = obj.to_dict()

        # Open the JSON file for writing
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            # Write the serialized objects to the file
            json.dump(serialized_objects, f)


    def reload(self):
        #  deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
        #  otherwise, do nothing. If the file doesn’t exist, no exception should be raised)

        if os.path.isfile(FileStorage.__file_path) is False:
            pass
        else:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = {}
                for k, v in obj_dict.items():
                    class_name = v["__class__"]
                    print(class_name)
                    class_constructor = self.classes()[class_name]
                    print(class_constructor)
                    reconstructed_object = class_constructor(**v)
                    print(reconstructed_object)
                    obj_dict[k] = reconstructed_object
                FileStorage.__objects = obj_dict
