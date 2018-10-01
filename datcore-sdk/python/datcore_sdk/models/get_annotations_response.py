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


class GetAnnotationsResponse(object):
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
        'annotations': 'dict(str, list[AnnotationDTO])',
        'layers': 'list[AnnotationLayer]',
        'user_map': 'dict(str, UserDTO)'
    }

    attribute_map = {
        'annotations': 'annotations',
        'layers': 'layers',
        'user_map': 'userMap'
    }

    def __init__(self, annotations=None, layers=None, user_map=None):  # noqa: E501
        """GetAnnotationsResponse - a model defined in OpenAPI"""  # noqa: E501

        self._annotations = None
        self._layers = None
        self._user_map = None
        self.discriminator = None

        self.annotations = annotations
        self.layers = layers
        self.user_map = user_map

    @property
    def annotations(self):
        """Gets the annotations of this GetAnnotationsResponse.  # noqa: E501


        :return: The annotations of this GetAnnotationsResponse.  # noqa: E501
        :rtype: dict(str, list[AnnotationDTO])
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this GetAnnotationsResponse.


        :param annotations: The annotations of this GetAnnotationsResponse.  # noqa: E501
        :type: dict(str, list[AnnotationDTO])
        """
        if annotations is None:
            raise ValueError("Invalid value for `annotations`, must not be `None`")  # noqa: E501

        self._annotations = annotations

    @property
    def layers(self):
        """Gets the layers of this GetAnnotationsResponse.  # noqa: E501


        :return: The layers of this GetAnnotationsResponse.  # noqa: E501
        :rtype: list[AnnotationLayer]
        """
        return self._layers

    @layers.setter
    def layers(self, layers):
        """Sets the layers of this GetAnnotationsResponse.


        :param layers: The layers of this GetAnnotationsResponse.  # noqa: E501
        :type: list[AnnotationLayer]
        """
        if layers is None:
            raise ValueError("Invalid value for `layers`, must not be `None`")  # noqa: E501

        self._layers = layers

    @property
    def user_map(self):
        """Gets the user_map of this GetAnnotationsResponse.  # noqa: E501


        :return: The user_map of this GetAnnotationsResponse.  # noqa: E501
        :rtype: dict(str, UserDTO)
        """
        return self._user_map

    @user_map.setter
    def user_map(self, user_map):
        """Sets the user_map of this GetAnnotationsResponse.


        :param user_map: The user_map of this GetAnnotationsResponse.  # noqa: E501
        :type: dict(str, UserDTO)
        """
        if user_map is None:
            raise ValueError("Invalid value for `user_map`, must not be `None`")  # noqa: E501

        self._user_map = user_map

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
        if not isinstance(other, GetAnnotationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
