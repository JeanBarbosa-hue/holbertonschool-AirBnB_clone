#!/usr/bin/python3
"""Module file_storage"""

import json
from models.base_model import BaseModel


class FileStorage:
    """
    Class for serializing instances to a JSON file and
    deserializing JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """A dictionary of objects is returned"""
        return self.__objects

    def new(self, obj):
        """The object is added to the object dictionary"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Objects are serialized and saved in a JSON file"""
        objects_dict = {}
        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Deserializes the JSON file to add objects to the list"""
        try:
            with open(self.__file_path, "r") as file:
                json_data = json.load(file)
                self.__objects.clear()
                for key, value in json_data.items():
                    self.__objects[key] = BaseModel(**value)
        except:
            pass
