#!/usr/bin/python3

import uuid
from datetime import datetime




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


    
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    

    def save(self):
        self.updated_at = datetime.now()

    
    def to_dict(self):
        dic = self.__dict__

        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = datetime.isoformat(self.created_at)
        dic['updated_at'] = datetime.isoformat(self.updated_at)
        return self.__dict__
