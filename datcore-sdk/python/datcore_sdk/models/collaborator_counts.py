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


class CollaboratorCounts(object):
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
        'users': 'int',
        'organizations': 'int',
        'teams': 'int'
    }

    attribute_map = {
        'users': 'users',
        'organizations': 'organizations',
        'teams': 'teams'
    }

    def __init__(self, users=None, organizations=None, teams=None):  # noqa: E501
        """CollaboratorCounts - a model defined in OpenAPI"""  # noqa: E501

        self._users = None
        self._organizations = None
        self._teams = None
        self.discriminator = None

        self.users = users
        self.organizations = organizations
        self.teams = teams

    @property
    def users(self):
        """Gets the users of this CollaboratorCounts.  # noqa: E501


        :return: The users of this CollaboratorCounts.  # noqa: E501
        :rtype: int
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this CollaboratorCounts.


        :param users: The users of this CollaboratorCounts.  # noqa: E501
        :type: int
        """
        if users is None:
            raise ValueError("Invalid value for `users`, must not be `None`")  # noqa: E501

        self._users = users

    @property
    def organizations(self):
        """Gets the organizations of this CollaboratorCounts.  # noqa: E501


        :return: The organizations of this CollaboratorCounts.  # noqa: E501
        :rtype: int
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this CollaboratorCounts.


        :param organizations: The organizations of this CollaboratorCounts.  # noqa: E501
        :type: int
        """
        if organizations is None:
            raise ValueError("Invalid value for `organizations`, must not be `None`")  # noqa: E501

        self._organizations = organizations

    @property
    def teams(self):
        """Gets the teams of this CollaboratorCounts.  # noqa: E501


        :return: The teams of this CollaboratorCounts.  # noqa: E501
        :rtype: int
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this CollaboratorCounts.


        :param teams: The teams of this CollaboratorCounts.  # noqa: E501
        :type: int
        """
        if teams is None:
            raise ValueError("Invalid value for `teams`, must not be `None`")  # noqa: E501

        self._teams = teams

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
        if not isinstance(other, CollaboratorCounts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
