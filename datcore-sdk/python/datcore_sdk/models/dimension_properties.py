# coding: utf-8

"""
    Blackfynn Swagger

    Swagger documentation for the Blackfynn api  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class DimensionProperties(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'resolution': 'float',
        'length': 'int',
        'unit': 'str',
        'assignment': 'DimensionAssignment'
    }

    attribute_map = {
        'name': 'name',
        'resolution': 'resolution',
        'length': 'length',
        'unit': 'unit',
        'assignment': 'assignment'
    }

    def __init__(self, name=None, resolution=None, length=None, unit=None, assignment=None):  # noqa: E501
        """DimensionProperties - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._resolution = None
        self._length = None
        self._unit = None
        self._assignment = None
        self.discriminator = None

        self.name = name
        if resolution is not None:
            self.resolution = resolution
        self.length = length
        if unit is not None:
            self.unit = unit
        self.assignment = assignment

    @property
    def name(self):
        """Gets the name of this DimensionProperties.  # noqa: E501


        :return: The name of this DimensionProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DimensionProperties.


        :param name: The name of this DimensionProperties.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def resolution(self):
        """Gets the resolution of this DimensionProperties.  # noqa: E501


        :return: The resolution of this DimensionProperties.  # noqa: E501
        :rtype: float
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this DimensionProperties.


        :param resolution: The resolution of this DimensionProperties.  # noqa: E501
        :type: float
        """

        self._resolution = resolution

    @property
    def length(self):
        """Gets the length of this DimensionProperties.  # noqa: E501


        :return: The length of this DimensionProperties.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this DimensionProperties.


        :param length: The length of this DimensionProperties.  # noqa: E501
        :type: int
        """
        if length is None:
            raise ValueError("Invalid value for `length`, must not be `None`")  # noqa: E501

        self._length = length

    @property
    def unit(self):
        """Gets the unit of this DimensionProperties.  # noqa: E501


        :return: The unit of this DimensionProperties.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this DimensionProperties.


        :param unit: The unit of this DimensionProperties.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def assignment(self):
        """Gets the assignment of this DimensionProperties.  # noqa: E501


        :return: The assignment of this DimensionProperties.  # noqa: E501
        :rtype: DimensionAssignment
        """
        return self._assignment

    @assignment.setter
    def assignment(self, assignment):
        """Sets the assignment of this DimensionProperties.


        :param assignment: The assignment of this DimensionProperties.  # noqa: E501
        :type: DimensionAssignment
        """
        if assignment is None:
            raise ValueError("Invalid value for `assignment`, must not be `None`")  # noqa: E501

        self._assignment = assignment

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DimensionProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
