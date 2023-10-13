#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new Place --")
my_user = Place()
my_user.save()
print(my_user)

print("-- Create a new Place 2 --")
my_user2 = Place()
my_user2.save()
print(my_user2)