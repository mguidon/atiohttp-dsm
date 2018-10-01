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


class Manifest(object):
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
        'type': 'PayloadType',
        'import_id': 'str',
        'organization_id': 'int',
        'content': 'Payload'
    }

    attribute_map = {
        'type': 'type',
        'import_id': 'importId',
        'organization_id': 'organizationId',
        'content': 'content'
    }

    def __init__(self, type=None, import_id=None, organization_id=None, content=None):  # noqa: E501
        """Manifest - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._import_id = None
        self._organization_id = None
        self._content = None
        self.discriminator = None

        self.type = type
        self.import_id = import_id
        self.organization_id = organization_id
        self.content = content

    @property
    def type(self):
        """Gets the type of this Manifest.  # noqa: E501


        :return: The type of this Manifest.  # noqa: E501
        :rtype: PayloadType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Manifest.


        :param type: The type of this Manifest.  # noqa: E501
        :type: PayloadType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def import_id(self):
        """Gets the import_id of this Manifest.  # noqa: E501


        :return: The import_id of this Manifest.  # noqa: E501
        :rtype: str
        """
        return self._import_id

    @import_id.setter
    def import_id(self, import_id):
        """Sets the import_id of this Manifest.


        :param import_id: The import_id of this Manifest.  # noqa: E501
        :type: str
        """
        if import_id is None:
            raise ValueError("Invalid value for `import_id`, must not be `None`")  # noqa: E501

        self._import_id = import_id

    @property
    def organization_id(self):
        """Gets the organization_id of this Manifest.  # noqa: E501


        :return: The organization_id of this Manifest.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Manifest.


        :param organization_id: The organization_id of this Manifest.  # noqa: E501
        :type: int
        """
        if organization_id is None:
            raise ValueError("Invalid value for `organization_id`, must not be `None`")  # noqa: E501

        self._organization_id = organization_id

    @property
    def content(self):
        """Gets the content of this Manifest.  # noqa: E501


        :return: The content of this Manifest.  # noqa: E501
        :rtype: Payload
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Manifest.


        :param content: The content of this Manifest.  # noqa: E501
        :type: Payload
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

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
        if not isinstance(other, Manifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
