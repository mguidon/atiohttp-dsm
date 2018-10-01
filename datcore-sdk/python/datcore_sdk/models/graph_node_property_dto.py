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


class GraphNodePropertyDTO(object):
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
        'hidden': 'bool',
        'key': 'str',
        'fixed': 'bool',
        'data_type': 'str',
        'value': 'Object',
        'display': 'str'
    }

    attribute_map = {
        'hidden': 'hidden',
        'key': 'key',
        'fixed': 'fixed',
        'data_type': 'dataType',
        'value': 'value',
        'display': 'display'
    }

    def __init__(self, hidden=None, key=None, fixed=None, data_type=None, value=None, display=None):  # noqa: E501
        """GraphNodePropertyDTO - a model defined in OpenAPI"""  # noqa: E501

        self._hidden = None
        self._key = None
        self._fixed = None
        self._data_type = None
        self._value = None
        self._display = None
        self.discriminator = None

        self.hidden = hidden
        self.key = key
        self.fixed = fixed
        self.data_type = data_type
        self.value = value
        self.display = display

    @property
    def hidden(self):
        """Gets the hidden of this GraphNodePropertyDTO.  # noqa: E501


        :return: The hidden of this GraphNodePropertyDTO.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this GraphNodePropertyDTO.


        :param hidden: The hidden of this GraphNodePropertyDTO.  # noqa: E501
        :type: bool
        """
        if hidden is None:
            raise ValueError("Invalid value for `hidden`, must not be `None`")  # noqa: E501

        self._hidden = hidden

    @property
    def key(self):
        """Gets the key of this GraphNodePropertyDTO.  # noqa: E501


        :return: The key of this GraphNodePropertyDTO.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this GraphNodePropertyDTO.


        :param key: The key of this GraphNodePropertyDTO.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def fixed(self):
        """Gets the fixed of this GraphNodePropertyDTO.  # noqa: E501


        :return: The fixed of this GraphNodePropertyDTO.  # noqa: E501
        :rtype: bool
        """
        return self._fixed

    @fixed.setter
    def fixed(self, fixed):
        """Sets the fixed of this GraphNodePropertyDTO.


        :param fixed: The fixed of this GraphNodePropertyDTO.  # noqa: E501
        :type: bool
        """
        if fixed is None:
            raise ValueError("Invalid value for `fixed`, must not be `None`")  # noqa: E501

        self._fixed = fixed

    @property
    def data_type(self):
        """Gets the data_type of this GraphNodePropertyDTO.  # noqa: E501


        :return: The data_type of this GraphNodePropertyDTO.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this GraphNodePropertyDTO.


        :param data_type: The data_type of this GraphNodePropertyDTO.  # noqa: E501
        :type: str
        """
        if data_type is None:
            raise ValueError("Invalid value for `data_type`, must not be `None`")  # noqa: E501

        self._data_type = data_type

    @property
    def value(self):
        """Gets the value of this GraphNodePropertyDTO.  # noqa: E501


        :return: The value of this GraphNodePropertyDTO.  # noqa: E501
        :rtype: Object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GraphNodePropertyDTO.


        :param value: The value of this GraphNodePropertyDTO.  # noqa: E501
        :type: Object
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def display(self):
        """Gets the display of this GraphNodePropertyDTO.  # noqa: E501


        :return: The display of this GraphNodePropertyDTO.  # noqa: E501
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this GraphNodePropertyDTO.


        :param display: The display of this GraphNodePropertyDTO.  # noqa: E501
        :type: str
        """
        if display is None:
            raise ValueError("Invalid value for `display`, must not be `None`")  # noqa: E501

        self._display = display

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
        if not isinstance(other, GraphNodePropertyDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
