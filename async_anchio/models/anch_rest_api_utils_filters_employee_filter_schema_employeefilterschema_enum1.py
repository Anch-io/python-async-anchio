# coding: utf-8

"""
    Anch.io

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Contact: opensource@anchio.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class AnchRestApiUtilsFiltersEmployeeFilterSchemaEmployeefilterschemaEnum1(str, Enum):
    """
    AnchRestApiUtilsFiltersEmployeeFilterSchemaEmployeefilterschemaEnum1
    """

    """
    allowed enum values
    """
    EMPTY = ''
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    ON_LEAVE = 'ON_LEAVE'
    TERMINATED = 'TERMINATED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AnchRestApiUtilsFiltersEmployeeFilterSchemaEmployeefilterschemaEnum1 from a JSON string"""
        return cls(json.loads(json_str))


