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


class ConsortiumResponse(object):
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
        'consortium': 'Consortium',
        'members': 'list[User]'
    }

    attribute_map = {
        'consortium': 'consortium',
        'members': 'members'
    }

    def __init__(self, consortium=None, members=None):  # noqa: E501
        """ConsortiumResponse - a model defined in OpenAPI"""  # noqa: E501

        self._consortium = None
        self._members = None
        self.discriminator = None

        self.consortium = consortium
        self.members = members

    @property
    def consortium(self):
        """Gets the consortium of this ConsortiumResponse.  # noqa: E501


        :return: The consortium of this ConsortiumResponse.  # noqa: E501
        :rtype: Consortium
        """
        return self._consortium

    @consortium.setter
    def consortium(self, consortium):
        """Sets the consortium of this ConsortiumResponse.


        :param consortium: The consortium of this ConsortiumResponse.  # noqa: E501
        :type: Consortium
        """
        if consortium is None:
            raise ValueError("Invalid value for `consortium`, must not be `None`")  # noqa: E501

        self._consortium = consortium

    @property
    def members(self):
        """Gets the members of this ConsortiumResponse.  # noqa: E501


        :return: The members of this ConsortiumResponse.  # noqa: E501
        :rtype: list[User]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this ConsortiumResponse.


        :param members: The members of this ConsortiumResponse.  # noqa: E501
        :type: list[User]
        """
        if members is None:
            raise ValueError("Invalid value for `members`, must not be `None`")  # noqa: E501

        self._members = members

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
        if not isinstance(other, ConsortiumResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other