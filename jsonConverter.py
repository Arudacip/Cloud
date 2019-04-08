import json
from flask import jsonify

class simpleJson(object):
     def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])
    

def convertToJson(**kwargs) -> str:
    return jsonify(simpleJson(kwargs).__dict__)
    pass