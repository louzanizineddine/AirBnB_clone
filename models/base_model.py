'''
!/usr/bin/python3
""" Class BaseModel"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """the base class"""

    def __init__(self, *args, **kwargs):
        """constructor"""
        if kwargs != {}:
            for key in kwargs:
                if key != "__class__":
                    if key in ['created_at', 'updated_at']:
                        self.__dict__[key] = datetime.strptime(
                            kwargs[key],
                            "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        clsname = self.__class__.__name__
        return f"[{clsname}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """dictionary containing all keys/values of __dict__ of the instance"""
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = dic['created_at'].isoformat()
        dic['updated_at'] = dic['updated_at'].isoformat()
        return dic
'''
#!/usr/bin/python3

"""Module for Base class
 Contains the Base class for the AirBnB clone console.
 """

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class for base model of object hierarchy."""
    def __init__(self, *args, **kwargs):
        """constructor"""
        if kwargs != {}:
            for key in kwargs:
                if key != "__class__":
                    if key in ['created_at', 'updated_at']:
                        self.__dict__[key] = datetime.strptime(
                            kwargs[key],
                            "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
    
    def __str__(self):
        """Returns a human-readable string representation
         of an instance."""

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute
         with the current datetime."""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an instance."""

        dic = self.__dict__.copy()

        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = dic['created_at'].isoformat()
        dic['updated_at'] = dic['updated_at'].isoformat()
        return dic
