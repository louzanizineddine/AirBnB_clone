import json

with open("file.json", "r", encoding="utf-8") as f:
    obj_dict = json.load(f)
    print(obj_dict)