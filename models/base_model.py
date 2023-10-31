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

    def __init__(self, updated_at):
        """Updating datetile"""
        self.updated_at = datetime.now()
        BaseModel.id = str(uuid.uuid4())

    def __str__(self):
        """ print a specifique format of informations nexpected"""
        return ("[{}] {} {}".format(self.__class__.__name__,
                                    self.id, self.__dict__))

    def save(self):
        """ Update the instance attribut update_at"""
        self.update_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keyand value"""
        my_dic = self.__dict__
        my_dic['__class__'] = self.__class__.__name__
        self.created_at = self.created_at.strtime('%Y-%m-%dT%H:%M:%S.%f')
        self.updated_at = self.updated_at.strtime('%Y-%m-%dT%H:%M:%S.%f')
        return my_dic
