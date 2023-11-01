#!/usr/bin/python3
""" The Class that define all common attributes
          and methodesf for other classe
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """ class BaseModel """

    id = str(uuid.uuid4())
    created_at = datetime.now()
    update_at = str(uuid.uuid4())

    def __init__(self, *args, **kwargs):
        """Updating datetile"""
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
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ print a specifique format of informations nexpected"""
        return ("[{}] {} {}".format(self.__class__.__name__,
                                    self.id, self.__dict__))

    def save(self):
        """ Update the instance attribut update_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keyand value"""
        my_dic = self.__dict__.copy()
        my_dic['__class__'] = self.__class__.__name__
        my_dic['created_at'] = datetime.isoformat(self.created_at)
        my_dic['updated_at'] = datetime.isoformat(self.updated_at)

        return my_dic
