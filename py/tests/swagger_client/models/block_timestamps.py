# coding: utf-8

"""
    Aeternity Epoch

    This is the [Aeternity](https://www.aeternity.com/) Epoch API.

    OpenAPI spec version: 1.0.0
    Contact: apiteam@aeternity.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BlockTimestamps(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'height': 'int',
        'ts': 'int',
        'delta_to_prev_block': 'int'
    }

    attribute_map = {
        'height': 'height',
        'ts': 'ts',
        'delta_to_prev_block': 'delta_to_prev_block'
    }

    def __init__(self, height=None, ts=None, delta_to_prev_block=None):
        """
        BlockTimestamps - a model defined in Swagger
        """

        self._height = None
        self._ts = None
        self._delta_to_prev_block = None

        if height is not None:
          self.height = height
        if ts is not None:
          self.ts = ts
        if delta_to_prev_block is not None:
          self.delta_to_prev_block = delta_to_prev_block

    @property
    def height(self):
        """
        Gets the height of this BlockTimestamps.

        :return: The height of this BlockTimestamps.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this BlockTimestamps.

        :param height: The height of this BlockTimestamps.
        :type: int
        """

        self._height = height

    @property
    def ts(self):
        """
        Gets the ts of this BlockTimestamps.

        :return: The ts of this BlockTimestamps.
        :rtype: int
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """
        Sets the ts of this BlockTimestamps.

        :param ts: The ts of this BlockTimestamps.
        :type: int
        """

        self._ts = ts

    @property
    def delta_to_prev_block(self):
        """
        Gets the delta_to_prev_block of this BlockTimestamps.

        :return: The delta_to_prev_block of this BlockTimestamps.
        :rtype: int
        """
        return self._delta_to_prev_block

    @delta_to_prev_block.setter
    def delta_to_prev_block(self, delta_to_prev_block):
        """
        Sets the delta_to_prev_block of this BlockTimestamps.

        :param delta_to_prev_block: The delta_to_prev_block of this BlockTimestamps.
        :type: int
        """

        self._delta_to_prev_block = delta_to_prev_block

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, BlockTimestamps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other