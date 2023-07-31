#!/usr/bin/python3
"""A function that returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """ Function that returns JSON representation(string)"""
    return json.dumps(my_obj)
