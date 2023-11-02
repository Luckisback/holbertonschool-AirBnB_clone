#!/usr/bin/python3
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


class FileStorage:
    """definition of the class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Methode that returns a filestroge's private attribut"""
        return FileStorage.__objects

    def new(self, obj):
        """Methode that creates the object format"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """"Methode that save to a json file """
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file)

    def reload(self):
        '''
        Method that deserializes the JSON file to __objects
        '''

        try:
            with open(FileStorage.__file_path, encoding="utf-8") as json_file2:
                new_dict = json.load(json_file2)
                cls = '__class__'
                for key, value in new_dict.items():
                    class_name = key.split('.')
                    FileStorage.__objects[key] = eval(value[cls] + '(**value)')
        except FileNotFoundError:
            pass
