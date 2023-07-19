#!/usr/bin/python3

"""Module containing class basemodel"""
import uuid
from datetime import datetime


class BaseModel:
    """class named basemodel"""

    def __init__(self, *args, **kwargs):
        """constructor method"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def updated(self):
        """update method"""
        self.updated_at = datetime.now()

    def __str__(self):
        """string method"""
        class_name = type(self).__name__
        return (f"[{class_name}] ({self.id}) {self.__dict__}")

    def save(self):
        """save updated info method"""
        self.updated_at = datetime.now()
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """convert dictionary method"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
