#!/usr/bin/python3

"""Module with class called Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class called Review"""
    place_id = ""
    user_id = ""
    text = ""
