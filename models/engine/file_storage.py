import json


class FileStorage:
    """Class for serializing instances to a JSON file and deserializing JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (__file_path)."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file (__file_path) to __objects (if the file exists)."""
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                from models.base_model import BaseModel
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    class_ = BaseModel if class_name == 'BaseModel' else None
                    if class_:
                        obj = class_(**value)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass
