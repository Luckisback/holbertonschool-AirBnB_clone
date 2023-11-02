i#!/usr/bin/python3
"""import for class FileStorage"""
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {"BaseModel": BaseModel}

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                value['created_at'] = datetime.strptime(value['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                value['updated_at'] = datetime.strptime(value['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                cls = models.classes[class_name]
                FileStorage.__objects[key] = cls(**value)

