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


class DatasetCopyRequest(object):
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
        'source_type': 'EntityType',
        'destination_type': 'EntityType',
        'source': 'int',
        'destination': 'int'
    }

    attribute_map = {
        'source_type': 'sourceType',
        'destination_type': 'destinationType',
        'source': 'source',
        'destination': 'destination'
    }

    def __init__(self, source_type=None, destination_type=None, source=None, destination=None):  # noqa: E501
        """DatasetCopyRequest - a model defined in OpenAPI"""  # noqa: E501

        self._source_type = None
        self._destination_type = None
        self._source = None
        self._destination = None
        self.discriminator = None

        self.source_type = source_type
        self.destination_type = destination_type
        self.source = source
        self.destination = destination

    @property
    def source_type(self):
        """Gets the source_type of this DatasetCopyRequest.  # noqa: E501


        :return: The source_type of this DatasetCopyRequest.  # noqa: E501
        :rtype: EntityType
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this DatasetCopyRequest.


        :param source_type: The source_type of this DatasetCopyRequest.  # noqa: E501
        :type: EntityType
        """
        if source_type is None:
            raise ValueError("Invalid value for `source_type`, must not be `None`")  # noqa: E501

        self._source_type = source_type

    @property
    def destination_type(self):
        """Gets the destination_type of this DatasetCopyRequest.  # noqa: E501


        :return: The destination_type of this DatasetCopyRequest.  # noqa: E501
        :rtype: EntityType
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """Sets the destination_type of this DatasetCopyRequest.


        :param destination_type: The destination_type of this DatasetCopyRequest.  # noqa: E501
        :type: EntityType
        """
        if destination_type is None:
            raise ValueError("Invalid value for `destination_type`, must not be `None`")  # noqa: E501

        self._destination_type = destination_type

    @property
    def source(self):
        """Gets the source of this DatasetCopyRequest.  # noqa: E501


        :return: The source of this DatasetCopyRequest.  # noqa: E501
        :rtype: int
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DatasetCopyRequest.


        :param source: The source of this DatasetCopyRequest.  # noqa: E501
        :type: int
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def destination(self):
        """Gets the destination of this DatasetCopyRequest.  # noqa: E501


        :return: The destination of this DatasetCopyRequest.  # noqa: E501
        :rtype: int
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this DatasetCopyRequest.


        :param destination: The destination of this DatasetCopyRequest.  # noqa: E501
        :type: int
        """
        if destination is None:
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        self._destination = destination

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
        if not isinstance(other, DatasetCopyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
