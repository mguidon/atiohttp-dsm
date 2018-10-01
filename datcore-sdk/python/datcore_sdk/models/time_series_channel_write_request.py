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


class TimeSeriesChannelWriteRequest(object):
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
        'rate': 'float',
        'name': 'str',
        'channel_type': 'str',
        'properties': 'list[GraphNodePropertyRO]',
        'end': 'int',
        'unit': 'str',
        'last_annotation': 'int',
        'spike_duration': 'int',
        'start': 'int',
        'group': 'str'
    }

    attribute_map = {
        'rate': 'rate',
        'name': 'name',
        'channel_type': 'channelType',
        'properties': 'properties',
        'end': 'end',
        'unit': 'unit',
        'last_annotation': 'lastAnnotation',
        'spike_duration': 'spikeDuration',
        'start': 'start',
        'group': 'group'
    }

    def __init__(self, rate=None, name=None, channel_type=None, properties=None, end=None, unit=None, last_annotation=None, spike_duration=None, start=None, group=None):  # noqa: E501
        """TimeSeriesChannelWriteRequest - a model defined in OpenAPI"""  # noqa: E501

        self._rate = None
        self._name = None
        self._channel_type = None
        self._properties = None
        self._end = None
        self._unit = None
        self._last_annotation = None
        self._spike_duration = None
        self._start = None
        self._group = None
        self.discriminator = None

        self.rate = rate
        self.name = name
        self.channel_type = channel_type
        self.properties = properties
        self.end = end
        self.unit = unit
        self.last_annotation = last_annotation
        if spike_duration is not None:
            self.spike_duration = spike_duration
        self.start = start
        if group is not None:
            self.group = group

    @property
    def rate(self):
        """Gets the rate of this TimeSeriesChannelWriteRequest.  # noqa: E501


        :return: The rate of this TimeSeriesChannelWriteRequest.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this TimeSeriesChannelWriteRequest.


        :param rate: The rate of this TimeSeriesChannelWriteRequest.  # noqa: E501
        :type: float
        """
        if rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")  # noqa: E501

        self._rate = rate

    @property
    def name(self):
        """Gets the name of this TimeSeriesChannelWriteRequest.  # noqa: E501


        :return: The name of this TimeSeriesChannelWriteRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TimeSeriesChannelWriteRequest.


        :param name: The name of this TimeSeriesChannelWriteRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def channel_type(self):
        """Gets the channel_type of this TimeSeriesChannelWriteRequest.  # noqa: E501


        :return: The channel_type of this TimeSeriesChannelWriteRequest.  # noqa: E501
        :rtype: str
        """
        return self._channel_type

    @channel_type.setter
    def channel_type(self, channel_type):
        """Sets the channel_type of this TimeSeriesChannelWriteRequest.


        :param channel_type: The channel_type of this TimeSeriesChannelWriteRequest.  # noqa: E501
        :type: str
        """
        if channel_type is None:
            raise ValueError("Invalid value for `channel_type`, must not be `None`")  # noqa: E501

        self._channel_type = channel_type

    @property
    def properties(self):
        """Gets the properties of this TimeSeriesChannelWriteRequest.  # noqa: E501


        :return: The properties of this TimeSeriesChannelWriteRequest.  # noqa: E501
        :rtype: list[GraphNodePropertyRO]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this TimeSeriesChannelWriteRequest.


        :param properties: The properties of this TimeSeriesChannelWriteRequest.  # noqa: E501
        :type: list[GraphNodePropertyRO]
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def end(self):
        """Gets the end of this TimeSeriesChannelWriteRequest.  # noqa: E501


        :return: The end of this TimeSeriesChannelWriteRequest.  # noqa: E501
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this TimeSeriesChannelWriteRequest.


        :param end: The end of this TimeSeriesChannelWriteRequest.  # noqa: E501
        :type: int
        """
        if end is None:
            raise ValueError("Invalid value for `end`, must not be `None`")  # noqa: E501

        self._end = end

    @property
    def unit(self):
        """Gets the unit of this TimeSeriesChannelWriteRequest.  # noqa: E501


        :return: The unit of this TimeSeriesChannelWriteRequest.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this TimeSeriesChannelWriteRequest.


        :param unit: The unit of this TimeSeriesChannelWriteRequest.  # noqa: E501
        :type: str
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit

    @property
    def last_annotation(self):
        """Gets the last_annotation of this TimeSeriesChannelWriteRequest.  # noqa: E501


        :return: The last_annotation of this TimeSeriesChannelWriteRequest.  # noqa: E501
        :rtype: int
        """
        return self._last_annotation

    @last_annotation.setter
    def last_annotation(self, last_annotation):
        """Sets the last_annotation of this TimeSeriesChannelWriteRequest.


        :param last_annotation: The last_annotation of this TimeSeriesChannelWriteRequest.  # noqa: E501
        :type: int
        """
        if last_annotation is None:
            raise ValueError("Invalid value for `last_annotation`, must not be `None`")  # noqa: E501

        self._last_annotation = last_annotation

    @property
    def spike_duration(self):
        """Gets the spike_duration of this TimeSeriesChannelWriteRequest.  # noqa: E501


        :return: The spike_duration of this TimeSeriesChannelWriteRequest.  # noqa: E501
        :rtype: int
        """
        return self._spike_duration

    @spike_duration.setter
    def spike_duration(self, spike_duration):
        """Sets the spike_duration of this TimeSeriesChannelWriteRequest.


        :param spike_duration: The spike_duration of this TimeSeriesChannelWriteRequest.  # noqa: E501
        :type: int
        """

        self._spike_duration = spike_duration

    @property
    def start(self):
        """Gets the start of this TimeSeriesChannelWriteRequest.  # noqa: E501


        :return: The start of this TimeSeriesChannelWriteRequest.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this TimeSeriesChannelWriteRequest.


        :param start: The start of this TimeSeriesChannelWriteRequest.  # noqa: E501
        :type: int
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def group(self):
        """Gets the group of this TimeSeriesChannelWriteRequest.  # noqa: E501


        :return: The group of this TimeSeriesChannelWriteRequest.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this TimeSeriesChannelWriteRequest.


        :param group: The group of this TimeSeriesChannelWriteRequest.  # noqa: E501
        :type: str
        """

        self._group = group

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
        if not isinstance(other, TimeSeriesChannelWriteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
