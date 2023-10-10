#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage



class BaseModel:

    def __init__(self, *args, **kwargs):

        if kwargs.__len__() != 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            else:
                self.id = str(uuid.uuid4())
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.created_at = datetime.now()
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)


    
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    
    def to_dict(self):
        dic = self.__dict__.copy()

        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = dic['created_at'].isoformat();
        dic['updated_at'] = dic['updated_at'].isoformat();
        return dic