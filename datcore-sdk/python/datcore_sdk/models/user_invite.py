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


class UserInvite(object):
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
        'updated_at': 'datetime',
        'email': 'str',
        'permission': 'DBPermission',
        'valid_until': 'datetime',
        'last_name': 'str',
        'first_name': 'str',
        'id': 'int',
        'token': 'str',
        'created_at': 'datetime',
        'organization_id': 'int',
        'node_id': 'str'
    }

    attribute_map = {
        'updated_at': 'updatedAt',
        'email': 'email',
        'permission': 'permission',
        'valid_until': 'validUntil',
        'last_name': 'lastName',
        'first_name': 'firstName',
        'id': 'id',
        'token': 'token',
        'created_at': 'createdAt',
        'organization_id': 'organizationId',
        'node_id': 'nodeId'
    }

    def __init__(self, updated_at=None, email=None, permission=None, valid_until=None, last_name=None, first_name=None, id=None, token=None, created_at=None, organization_id=None, node_id=None):  # noqa: E501
        """UserInvite - a model defined in OpenAPI"""  # noqa: E501

        self._updated_at = None
        self._email = None
        self._permission = None
        self._valid_until = None
        self._last_name = None
        self._first_name = None
        self._id = None
        self._token = None
        self._created_at = None
        self._organization_id = None
        self._node_id = None
        self.discriminator = None

        self.updated_at = updated_at
        self.email = email
        self.permission = permission
        self.valid_until = valid_until
        self.last_name = last_name
        self.first_name = first_name
        self.id = id
        self.token = token
        self.created_at = created_at
        self.organization_id = organization_id
        self.node_id = node_id

    @property
    def updated_at(self):
        """Gets the updated_at of this UserInvite.  # noqa: E501


        :return: The updated_at of this UserInvite.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UserInvite.


        :param updated_at: The updated_at of this UserInvite.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def email(self):
        """Gets the email of this UserInvite.  # noqa: E501


        :return: The email of this UserInvite.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserInvite.


        :param email: The email of this UserInvite.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def permission(self):
        """Gets the permission of this UserInvite.  # noqa: E501


        :return: The permission of this UserInvite.  # noqa: E501
        :rtype: DBPermission
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this UserInvite.


        :param permission: The permission of this UserInvite.  # noqa: E501
        :type: DBPermission
        """
        if permission is None:
            raise ValueError("Invalid value for `permission`, must not be `None`")  # noqa: E501

        self._permission = permission

    @property
    def valid_until(self):
        """Gets the valid_until of this UserInvite.  # noqa: E501


        :return: The valid_until of this UserInvite.  # noqa: E501
        :rtype: datetime
        """
        return self._valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        """Sets the valid_until of this UserInvite.


        :param valid_until: The valid_until of this UserInvite.  # noqa: E501
        :type: datetime
        """
        if valid_until is None:
            raise ValueError("Invalid value for `valid_until`, must not be `None`")  # noqa: E501

        self._valid_until = valid_until

    @property
    def last_name(self):
        """Gets the last_name of this UserInvite.  # noqa: E501


        :return: The last_name of this UserInvite.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserInvite.


        :param last_name: The last_name of this UserInvite.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def first_name(self):
        """Gets the first_name of this UserInvite.  # noqa: E501


        :return: The first_name of this UserInvite.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserInvite.


        :param first_name: The first_name of this UserInvite.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def id(self):
        """Gets the id of this UserInvite.  # noqa: E501


        :return: The id of this UserInvite.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserInvite.


        :param id: The id of this UserInvite.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def token(self):
        """Gets the token of this UserInvite.  # noqa: E501


        :return: The token of this UserInvite.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UserInvite.


        :param token: The token of this UserInvite.  # noqa: E501
        :type: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def created_at(self):
        """Gets the created_at of this UserInvite.  # noqa: E501


        :return: The created_at of this UserInvite.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserInvite.


        :param created_at: The created_at of this UserInvite.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def organization_id(self):
        """Gets the organization_id of this UserInvite.  # noqa: E501


        :return: The organization_id of this UserInvite.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this UserInvite.


        :param organization_id: The organization_id of this UserInvite.  # noqa: E501
        :type: int
        """
        if organization_id is None:
            raise ValueError("Invalid value for `organization_id`, must not be `None`")  # noqa: E501

        self._organization_id = organization_id

    @property
    def node_id(self):
        """Gets the node_id of this UserInvite.  # noqa: E501


        :return: The node_id of this UserInvite.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this UserInvite.


        :param node_id: The node_id of this UserInvite.  # noqa: E501
        :type: str
        """
        if node_id is None:
            raise ValueError("Invalid value for `node_id`, must not be `None`")  # noqa: E501

        self._node_id = node_id

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
        if not isinstance(other, UserInvite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
