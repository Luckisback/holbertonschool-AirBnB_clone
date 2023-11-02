#!/usr/bin/python3
"""
The Class that defines all common attributes
and methods for other classes
"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """
    class BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    self.updated_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "my_number":
                    self.my_number = value
                if key == "name":
                    self.name = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the object.
        """
        return ("[{}] {} {}".format(self.__class__.__name__,
                                    self.id, self.__dict__))

    def save(self):
        """
        Updates the instance's updated_at attribute.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all key and value.
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()

        return my_dict

