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


class OrganizationDTO(object):
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
        'encryption_key_id': 'str',
        'features': 'list[Feature]',
        'int_id': 'int',
        'slug': 'str',
        'id': 'str',
        'storage': 'int',
        'subscription_state': 'SubscriptionStateDTO',
        'terms': 'str'
    }

    attribute_map = {
        'name': 'name',
        'encryption_key_id': 'encryptionKeyId',
        'features': 'features',
        'int_id': 'intId',
        'slug': 'slug',
        'id': 'id',
        'storage': 'storage',
        'subscription_state': 'subscriptionState',
        'terms': 'terms'
    }

    def __init__(self, name=None, encryption_key_id=None, features=None, int_id=None, slug=None, id=None, storage=None, subscription_state=None, terms=None):  # noqa: E501
        """OrganizationDTO - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._encryption_key_id = None
        self._features = None
        self._int_id = None
        self._slug = None
        self._id = None
        self._storage = None
        self._subscription_state = None
        self._terms = None
        self.discriminator = None

        self.name = name
        self.encryption_key_id = encryption_key_id
        self.features = features
        self.int_id = int_id
        self.slug = slug
        self.id = id
        if storage is not None:
            self.storage = storage
        self.subscription_state = subscription_state
        if terms is not None:
            self.terms = terms

    @property
    def name(self):
        """Gets the name of this OrganizationDTO.  # noqa: E501


        :return: The name of this OrganizationDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationDTO.


        :param name: The name of this OrganizationDTO.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def encryption_key_id(self):
        """Gets the encryption_key_id of this OrganizationDTO.  # noqa: E501


        :return: The encryption_key_id of this OrganizationDTO.  # noqa: E501
        :rtype: str
        """
        return self._encryption_key_id

    @encryption_key_id.setter
    def encryption_key_id(self, encryption_key_id):
        """Sets the encryption_key_id of this OrganizationDTO.


        :param encryption_key_id: The encryption_key_id of this OrganizationDTO.  # noqa: E501
        :type: str
        """
        if encryption_key_id is None:
            raise ValueError("Invalid value for `encryption_key_id`, must not be `None`")  # noqa: E501

        self._encryption_key_id = encryption_key_id

    @property
    def features(self):
        """Gets the features of this OrganizationDTO.  # noqa: E501


        :return: The features of this OrganizationDTO.  # noqa: E501
        :rtype: list[Feature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this OrganizationDTO.


        :param features: The features of this OrganizationDTO.  # noqa: E501
        :type: list[Feature]
        """
        if features is None:
            raise ValueError("Invalid value for `features`, must not be `None`")  # noqa: E501

        self._features = features

    @property
    def int_id(self):
        """Gets the int_id of this OrganizationDTO.  # noqa: E501


        :return: The int_id of this OrganizationDTO.  # noqa: E501
        :rtype: int
        """
        return self._int_id

    @int_id.setter
    def int_id(self, int_id):
        """Sets the int_id of this OrganizationDTO.


        :param int_id: The int_id of this OrganizationDTO.  # noqa: E501
        :type: int
        """
        if int_id is None:
            raise ValueError("Invalid value for `int_id`, must not be `None`")  # noqa: E501

        self._int_id = int_id

    @property
    def slug(self):
        """Gets the slug of this OrganizationDTO.  # noqa: E501


        :return: The slug of this OrganizationDTO.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this OrganizationDTO.


        :param slug: The slug of this OrganizationDTO.  # noqa: E501
        :type: str
        """
        if slug is None:
            raise ValueError("Invalid value for `slug`, must not be `None`")  # noqa: E501

        self._slug = slug

    @property
    def id(self):
        """Gets the id of this OrganizationDTO.  # noqa: E501


        :return: The id of this OrganizationDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganizationDTO.


        :param id: The id of this OrganizationDTO.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def storage(self):
        """Gets the storage of this OrganizationDTO.  # noqa: E501


        :return: The storage of this OrganizationDTO.  # noqa: E501
        :rtype: int
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this OrganizationDTO.


        :param storage: The storage of this OrganizationDTO.  # noqa: E501
        :type: int
        """

        self._storage = storage

    @property
    def subscription_state(self):
        """Gets the subscription_state of this OrganizationDTO.  # noqa: E501


        :return: The subscription_state of this OrganizationDTO.  # noqa: E501
        :rtype: SubscriptionStateDTO
        """
        return self._subscription_state

    @subscription_state.setter
    def subscription_state(self, subscription_state):
        """Sets the subscription_state of this OrganizationDTO.


        :param subscription_state: The subscription_state of this OrganizationDTO.  # noqa: E501
        :type: SubscriptionStateDTO
        """
        if subscription_state is None:
            raise ValueError("Invalid value for `subscription_state`, must not be `None`")  # noqa: E501

        self._subscription_state = subscription_state

    @property
    def terms(self):
        """Gets the terms of this OrganizationDTO.  # noqa: E501


        :return: The terms of this OrganizationDTO.  # noqa: E501
        :rtype: str
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this OrganizationDTO.


        :param terms: The terms of this OrganizationDTO.  # noqa: E501
        :type: str
        """

        self._terms = terms

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
        if not isinstance(other, OrganizationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
