#!/usr/bin/python3
"""Module file_storage"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


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
                    class_name = value['__class__']
                    if class_name == 'User':
                        self.__objects[key] = User(**value)
                    elif class_name == 'Place':
                        self.__objects[key] = Place(**value)
                    elif class_name == 'State':
                        self.__objects[key] = State(**value)
                    elif class_name == 'City':
                        self.__objects[key] = City(**value)
                    elif class_name == 'Amenity':
                        self.__objects[key] = Amenity(**value)
                    elif class_name == 'Review':
                        self.__objects[key] = Review(**value)
                    else:
                        self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
