#!/usr/bin/python3

"""Module containing class basemodel"""
import uuid
from datetime import datetime


class BaseModel:
    """class named basemodel"""

    def __init__(self):
        """constructor metohod"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def updated(self):
        """update method"""
        self.updated_at = datetime.now()

    def __str__(self):
        """string method"""
        return (f"[{self.__class__.__name}] ({self.id}) {self.__dict__}")

    def save(self):
        """save updated info method"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """convert dictionary method"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
