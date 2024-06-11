# coding: utf-8

"""
    Anch.io

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.2
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


class AnchRestApiUtilsFiltersEmployeeFilterSchemaEmployeefilterschemaEnum2(str, Enum):
    """
    AnchRestApiUtilsFiltersEmployeeFilterSchemaEmployeefilterschemaEnum2
    """

    """
    allowed enum values
    """
    EMPTY = ''
    FULL_TIME = 'FULL_TIME'
    CONTRACT = 'CONTRACT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AnchRestApiUtilsFiltersEmployeeFilterSchemaEmployeefilterschemaEnum2 from a JSON string"""
        return cls(json.loads(json_str))


