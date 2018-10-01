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


class CreateLedgerEntryRequest(object):
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
        'reference': 'str',
        'dataset_id': 'str',
        'date': 'datetime',
        'metric': 'str',
        'organization_id': 'str',
        'user_id': 'str',
        'value': 'float'
    }

    attribute_map = {
        'reference': 'reference',
        'dataset_id': 'datasetId',
        'date': 'date',
        'metric': 'metric',
        'organization_id': 'organizationId',
        'user_id': 'userId',
        'value': 'value'
    }

    def __init__(self, reference=None, dataset_id=None, date=None, metric=None, organization_id=None, user_id=None, value=None):  # noqa: E501
        """CreateLedgerEntryRequest - a model defined in OpenAPI"""  # noqa: E501

        self._reference = None
        self._dataset_id = None
        self._date = None
        self._metric = None
        self._organization_id = None
        self._user_id = None
        self._value = None
        self.discriminator = None

        self.reference = reference
        if dataset_id is not None:
            self.dataset_id = dataset_id
        self.date = date
        self.metric = metric
        self.organization_id = organization_id
        if user_id is not None:
            self.user_id = user_id
        self.value = value

    @property
    def reference(self):
        """Gets the reference of this CreateLedgerEntryRequest.  # noqa: E501


        :return: The reference of this CreateLedgerEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this CreateLedgerEntryRequest.


        :param reference: The reference of this CreateLedgerEntryRequest.  # noqa: E501
        :type: str
        """
        if reference is None:
            raise ValueError("Invalid value for `reference`, must not be `None`")  # noqa: E501

        self._reference = reference

    @property
    def dataset_id(self):
        """Gets the dataset_id of this CreateLedgerEntryRequest.  # noqa: E501


        :return: The dataset_id of this CreateLedgerEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this CreateLedgerEntryRequest.


        :param dataset_id: The dataset_id of this CreateLedgerEntryRequest.  # noqa: E501
        :type: str
        """

        self._dataset_id = dataset_id

    @property
    def date(self):
        """Gets the date of this CreateLedgerEntryRequest.  # noqa: E501


        :return: The date of this CreateLedgerEntryRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this CreateLedgerEntryRequest.


        :param date: The date of this CreateLedgerEntryRequest.  # noqa: E501
        :type: datetime
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def metric(self):
        """Gets the metric of this CreateLedgerEntryRequest.  # noqa: E501


        :return: The metric of this CreateLedgerEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this CreateLedgerEntryRequest.


        :param metric: The metric of this CreateLedgerEntryRequest.  # noqa: E501
        :type: str
        """
        if metric is None:
            raise ValueError("Invalid value for `metric`, must not be `None`")  # noqa: E501

        self._metric = metric

    @property
    def organization_id(self):
        """Gets the organization_id of this CreateLedgerEntryRequest.  # noqa: E501


        :return: The organization_id of this CreateLedgerEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this CreateLedgerEntryRequest.


        :param organization_id: The organization_id of this CreateLedgerEntryRequest.  # noqa: E501
        :type: str
        """
        if organization_id is None:
            raise ValueError("Invalid value for `organization_id`, must not be `None`")  # noqa: E501

        self._organization_id = organization_id

    @property
    def user_id(self):
        """Gets the user_id of this CreateLedgerEntryRequest.  # noqa: E501


        :return: The user_id of this CreateLedgerEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CreateLedgerEntryRequest.


        :param user_id: The user_id of this CreateLedgerEntryRequest.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def value(self):
        """Gets the value of this CreateLedgerEntryRequest.  # noqa: E501


        :return: The value of this CreateLedgerEntryRequest.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CreateLedgerEntryRequest.


        :param value: The value of this CreateLedgerEntryRequest.  # noqa: E501
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, CreateLedgerEntryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
