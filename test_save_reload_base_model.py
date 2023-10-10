#!/usr/bin/python3


from models.base_model import BaseModel
from models import storage
print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "test"
my_model.my_number = 23
my_model.save()
print(my_model)


print("-- Create a new object --")
my_model1 = BaseModel()
my_model1.name = "test2"
my_model1.my_number = 27
my_model1.save()
print(my_model1)

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

