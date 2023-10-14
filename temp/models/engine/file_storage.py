#!/usr/bin/python3
"""Module for FileStorage class."""
import json
import os


class FileStorage:
    """Class for serializtion and deserialization of base classes."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns dic of __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Class for serializtion and deserialization of base classes."""

        serialized_objects = {}

        ''' Iterate through the objects in FileStorage.__objects'''
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes JSON file into __objects."""

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
                dic = json.load(f)

                for k, v in dic.items():
                    class_name = v["__class__"]
                    match class_name:
                        case 'User':
                            # create a new User
                            dic[k] = User(**v)
                            # check if the key is in the dictionary
                            # if it is, update the value
                            # if not, create a new key-value pair

                            if "first_name" in v:
                                dic[k].firs_name = v["first_name"]
                            if "last_name" in v:
                                dic[k].last_name = v["last_name"]
                            if "email" in v:
                                dic[k].email = v["email"]
                            if "password" in v:
                                dic[k].password = v["password"]

                        case 'BaseModel':
                            dic[k] = BaseModel(**v)

                        case 'Place':
                            dic[k] = Place(**v)
                            if "name" in v:
                                dic[k].name = v["name"]
                            if "city_id" in v:
                                dic[k].city_id = v["city_id"]
                            if "user_id" in v:
                                dic[k].user_id = v["user_id"]
                            if "description" in v:
                                dic[k].description = v["description"]
                            if "number_rooms" in v:
                                dic[k].number_rooms = v["number_rooms"]
                            if "number_bathrooms" in v:
                                dic[k].number_bathrooms = v["number_bathrooms"]
                            if "max_guest" in v:
                                dic[k].max_guest = v["max_guest"]
                            if "price_by_night" in v:
                                dic[k].price_by_night = v["price_by_night"]
                            if "latitude" in v:
                                dic[k].latitude = v["latitude"]
                            if "longitude" in v:
                                dic[k].longitude = v["longitude"]

                        case 'State':
                            dic[k] = State(**v)
                            if "name" in v:
                                dic[k].name = v["name"]

                        case 'Review':
                            dic[k] = Review(**v)
                            if "place_id" in v:
                                dic[k].place_id = v["place_id"]
                            if "user_id" in v:
                                dic[k].user_id = v["user_id"]
                            if "text" in v:
                                dic[k].text = v["text"]

                        case 'City':
                            dic[k] = City(**v)
                            if "name" in v:
                                dic[k].name = v["name"]
                            if "state_id" in v:
                                dic[k].state_id = v["state_id"]

                        case 'Amenity':
                            dic[k] = City(**v)

                            if "name" in v:
                                dic[k].name = v["name"]

                FileStorage.__objects = dic
