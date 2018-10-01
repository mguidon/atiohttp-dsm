# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from .base_model_ import Model
from .. import util


class ErrorModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, errors=None):  # noqa: E501
        """ErrorModel - a model defined in OpenAPI

        :param errors: The errors of this ErrorModel.  # noqa: E501
        :type errors: List[str]
        """
        self.openapi_types = {
            'errors': 'List[str]'
        }

        self.attribute_map = {
            'errors': 'errors'
        }

        self._errors = errors

    @classmethod
    def from_dict(cls, dikt) -> 'ErrorModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ErrorModel of this ErrorModel.  # noqa: E501
        :rtype: ErrorModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def errors(self):
        """Gets the errors of this ErrorModel.


        :return: The errors of this ErrorModel.
        :rtype: List[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ErrorModel.


        :param errors: The errors of this ErrorModel.
        :type errors: List[str]
        """

        self._errors = errors
