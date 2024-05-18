#!/usr/bin/python3
"""This is the FileStorage module"""

import json
import os


class FileStorage():
    """The class FileStorage that serializes and deserializes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_s = {}
        for key, val in self.__objects.items():
            obj_s[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as afile:
            json.dump(obj_s, afile)

    def reload(self):
        """Deserializes the JSON file to __objects only if the file exists"""
        from models.base_model import BaseModel
        from models.user import User
        c_dict = {'BaseModel': BaseModel, 'User': User}

        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r', encoding='utf-8') as afile:
                    obj_d = json.load(afile)
                    for key, val in obj_d.items():
                        c_name = c_dict[val['__class__']](**val)
                        self.__objects[key] = c_name
            except FileNotFoundError:
                pass
