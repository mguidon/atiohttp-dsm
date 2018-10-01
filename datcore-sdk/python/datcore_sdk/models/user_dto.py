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


class UserDTO(object):
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
        'email': 'str',
        'url': 'str',
        'is_super_admin': 'bool',
        'color': 'str',
        'last_name': 'str',
        'is_owner': 'bool',
        'first_name': 'str',
        'id': 'str',
        'authy_id': 'int',
        'preferred_organization': 'str',
        'storage': 'int',
        'credential': 'str'
    }

    attribute_map = {
        'email': 'email',
        'url': 'url',
        'is_super_admin': 'isSuperAdmin',
        'color': 'color',
        'last_name': 'lastName',
        'is_owner': 'isOwner',
        'first_name': 'firstName',
        'id': 'id',
        'authy_id': 'authyId',
        'preferred_organization': 'preferredOrganization',
        'storage': 'storage',
        'credential': 'credential'
    }

    def __init__(self, email=None, url=None, is_super_admin=None, color=None, last_name=None, is_owner=None, first_name=None, id=None, authy_id=None, preferred_organization=None, storage=None, credential=None):  # noqa: E501
        """UserDTO - a model defined in OpenAPI"""  # noqa: E501

        self._email = None
        self._url = None
        self._is_super_admin = None
        self._color = None
        self._last_name = None
        self._is_owner = None
        self._first_name = None
        self._id = None
        self._authy_id = None
        self._preferred_organization = None
        self._storage = None
        self._credential = None
        self.discriminator = None

        self.email = email
        self.url = url
        self.is_super_admin = is_super_admin
        self.color = color
        self.last_name = last_name
        if is_owner is not None:
            self.is_owner = is_owner
        self.first_name = first_name
        self.id = id
        self.authy_id = authy_id
        if preferred_organization is not None:
            self.preferred_organization = preferred_organization
        if storage is not None:
            self.storage = storage
        self.credential = credential

    @property
    def email(self):
        """Gets the email of this UserDTO.  # noqa: E501


        :return: The email of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserDTO.


        :param email: The email of this UserDTO.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def url(self):
        """Gets the url of this UserDTO.  # noqa: E501


        :return: The url of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UserDTO.


        :param url: The url of this UserDTO.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def is_super_admin(self):
        """Gets the is_super_admin of this UserDTO.  # noqa: E501


        :return: The is_super_admin of this UserDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_super_admin

    @is_super_admin.setter
    def is_super_admin(self, is_super_admin):
        """Sets the is_super_admin of this UserDTO.


        :param is_super_admin: The is_super_admin of this UserDTO.  # noqa: E501
        :type: bool
        """
        if is_super_admin is None:
            raise ValueError("Invalid value for `is_super_admin`, must not be `None`")  # noqa: E501

        self._is_super_admin = is_super_admin

    @property
    def color(self):
        """Gets the color of this UserDTO.  # noqa: E501


        :return: The color of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this UserDTO.


        :param color: The color of this UserDTO.  # noqa: E501
        :type: str
        """
        if color is None:
            raise ValueError("Invalid value for `color`, must not be `None`")  # noqa: E501

        self._color = color

    @property
    def last_name(self):
        """Gets the last_name of this UserDTO.  # noqa: E501


        :return: The last_name of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserDTO.


        :param last_name: The last_name of this UserDTO.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def is_owner(self):
        """Gets the is_owner of this UserDTO.  # noqa: E501


        :return: The is_owner of this UserDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_owner

    @is_owner.setter
    def is_owner(self, is_owner):
        """Sets the is_owner of this UserDTO.


        :param is_owner: The is_owner of this UserDTO.  # noqa: E501
        :type: bool
        """

        self._is_owner = is_owner

    @property
    def first_name(self):
        """Gets the first_name of this UserDTO.  # noqa: E501


        :return: The first_name of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserDTO.


        :param first_name: The first_name of this UserDTO.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def id(self):
        """Gets the id of this UserDTO.  # noqa: E501


        :return: The id of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserDTO.


        :param id: The id of this UserDTO.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def authy_id(self):
        """Gets the authy_id of this UserDTO.  # noqa: E501


        :return: The authy_id of this UserDTO.  # noqa: E501
        :rtype: int
        """
        return self._authy_id

    @authy_id.setter
    def authy_id(self, authy_id):
        """Sets the authy_id of this UserDTO.


        :param authy_id: The authy_id of this UserDTO.  # noqa: E501
        :type: int
        """
        if authy_id is None:
            raise ValueError("Invalid value for `authy_id`, must not be `None`")  # noqa: E501

        self._authy_id = authy_id

    @property
    def preferred_organization(self):
        """Gets the preferred_organization of this UserDTO.  # noqa: E501


        :return: The preferred_organization of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._preferred_organization

    @preferred_organization.setter
    def preferred_organization(self, preferred_organization):
        """Sets the preferred_organization of this UserDTO.


        :param preferred_organization: The preferred_organization of this UserDTO.  # noqa: E501
        :type: str
        """

        self._preferred_organization = preferred_organization

    @property
    def storage(self):
        """Gets the storage of this UserDTO.  # noqa: E501


        :return: The storage of this UserDTO.  # noqa: E501
        :rtype: int
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this UserDTO.


        :param storage: The storage of this UserDTO.  # noqa: E501
        :type: int
        """

        self._storage = storage

    @property
    def credential(self):
        """Gets the credential of this UserDTO.  # noqa: E501


        :return: The credential of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        """Sets the credential of this UserDTO.


        :param credential: The credential of this UserDTO.  # noqa: E501
        :type: str
        """
        if credential is None:
            raise ValueError("Invalid value for `credential`, must not be `None`")  # noqa: E501

        self._credential = credential

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
        if not isinstance(other, UserDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other