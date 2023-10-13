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
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review


        if os.path.isfile(FileStorage.__file_path) is False:
            pass
        else:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                
                for k, v in obj_dict.items():
                    class_name = v["__class__"]
                    match class_name:
                        case 'User':
                            # create a new User
                            obj_dict[k] = User(**v)
                            # check if the key is in the dictionary
                            # if it is, update the value
                            # if not, create a new key-value pair

                            if "first_name" in v:
                                obj_dict[k].firs_name = v["first_name"]
                            if "last_name" in v:
                                obj_dict[k].last_name = v["last_name"]
                            if "email" in v:
                                obj_dict[k].email = v["email"]
                            if "password" in v:
                                obj_dict[k].password = v["password"]
                    
                        case 'BaseModel':
                            obj_dict[k] = BaseModel(**v)

                        case 'Place':
                            obj_dict[k] = Place(**v)
                            if "name" in v:
                                obj_dict[k].name = v["name"]
                            if "city_id" in v:
                                obj_dict[k].city_id = v["city_id"]
                            if "user_id" in v:
                                obj_dict[k].user_id = v["user_id"]
                            if "description" in v:
                                obj_dict[k].description = v["description"]
                            if "number_rooms" in v:
                                obj_dict[k].number_rooms = v["number_rooms"]
                            if "number_bathrooms" in v:
                                obj_dict[k].number_bathrooms = v["number_bathrooms"]
                            if "max_guest" in v:
                                obj_dict[k].max_guest = v["max_guest"]
                            if "price_by_night" in v:
                                obj_dict[k].price_by_night = v["price_by_night"]
                            if "latitude" in v:
                                obj_dict[k].latitude = v["latitude"]
                            if "longitude" in v:
                                obj_dict[k].longitude = v["longitude"]

                        case 'State':
                            obj_dict[k] = State(**v)
                            if "name" in v:
                                obj_dict[k].name = v["name"]
              
                        case 'Review':
                            obj_dict[k] = Review(**v)
                            if "place_id" in v:
                                obj_dict[k].place_id = v["place_id"]
                            if "user_id" in v:
                                obj_dict[k].user_id = v["user_id"]
                            if "text" in v:
                                obj_dict[k].text = v["text"]
                        
                        case 'City':
                            obj_dict[k] = City(**v)
                            if "name" in v:
                                obj_dict[k].name = v["name"]
                            
                            if "state_id" in v:
                                obj_dict[k].state_id = v["state_id"]

                        case 'Amenity':
                            obj_dict[k] = City(**v)

                            if "name" in v:
                                obj_dict[k].name = v["name"]

                FileStorage.__objects = obj_dict
