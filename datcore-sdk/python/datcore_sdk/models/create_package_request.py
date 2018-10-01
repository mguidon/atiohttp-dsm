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


class CreatePackageRequest(object):
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
        'parent': 'str',
        'name': 'str',
        'state': 'PackageState',
        'package_type': 'PackageType',
        'properties': 'list[GraphNodePropertyRO]',
        'dataset': 'str',
        'owner': 'str'
    }

    attribute_map = {
        'parent': 'parent',
        'name': 'name',
        'state': 'state',
        'package_type': 'packageType',
        'properties': 'properties',
        'dataset': 'dataset',
        'owner': 'owner'
    }

    def __init__(self, parent=None, name=None, state=None, package_type=None, properties=None, dataset=None, owner=None):  # noqa: E501
        """CreatePackageRequest - a model defined in OpenAPI"""  # noqa: E501

        self._parent = None
        self._name = None
        self._state = None
        self._package_type = None
        self._properties = None
        self._dataset = None
        self._owner = None
        self.discriminator = None

        if parent is not None:
            self.parent = parent
        self.name = name
        if state is not None:
            self.state = state
        self.package_type = package_type
        self.properties = properties
        self.dataset = dataset
        if owner is not None:
            self.owner = owner

    @property
    def parent(self):
        """Gets the parent of this CreatePackageRequest.  # noqa: E501


        :return: The parent of this CreatePackageRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this CreatePackageRequest.


        :param parent: The parent of this CreatePackageRequest.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def name(self):
        """Gets the name of this CreatePackageRequest.  # noqa: E501


        :return: The name of this CreatePackageRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePackageRequest.


        :param name: The name of this CreatePackageRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def state(self):
        """Gets the state of this CreatePackageRequest.  # noqa: E501


        :return: The state of this CreatePackageRequest.  # noqa: E501
        :rtype: PackageState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CreatePackageRequest.


        :param state: The state of this CreatePackageRequest.  # noqa: E501
        :type: PackageState
        """

        self._state = state

    @property
    def package_type(self):
        """Gets the package_type of this CreatePackageRequest.  # noqa: E501


        :return: The package_type of this CreatePackageRequest.  # noqa: E501
        :rtype: PackageType
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """Sets the package_type of this CreatePackageRequest.


        :param package_type: The package_type of this CreatePackageRequest.  # noqa: E501
        :type: PackageType
        """
        if package_type is None:
            raise ValueError("Invalid value for `package_type`, must not be `None`")  # noqa: E501

        self._package_type = package_type

    @property
    def properties(self):
        """Gets the properties of this CreatePackageRequest.  # noqa: E501


        :return: The properties of this CreatePackageRequest.  # noqa: E501
        :rtype: list[GraphNodePropertyRO]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this CreatePackageRequest.


        :param properties: The properties of this CreatePackageRequest.  # noqa: E501
        :type: list[GraphNodePropertyRO]
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def dataset(self):
        """Gets the dataset of this CreatePackageRequest.  # noqa: E501


        :return: The dataset of this CreatePackageRequest.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this CreatePackageRequest.


        :param dataset: The dataset of this CreatePackageRequest.  # noqa: E501
        :type: str
        """
        if dataset is None:
            raise ValueError("Invalid value for `dataset`, must not be `None`")  # noqa: E501

        self._dataset = dataset

    @property
    def owner(self):
        """Gets the owner of this CreatePackageRequest.  # noqa: E501


        :return: The owner of this CreatePackageRequest.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this CreatePackageRequest.


        :param owner: The owner of this CreatePackageRequest.  # noqa: E501
        :type: str
        """

        self._owner = owner

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
        if not isinstance(other, CreatePackageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
