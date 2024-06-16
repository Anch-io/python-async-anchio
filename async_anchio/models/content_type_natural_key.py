# coding: utf-8

"""
    Anch.io

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.5
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


class ContentTypeNaturalKey(str, Enum):
    """
    ContentTypeNaturalKey
    """

    """
    allowed enum values
    """
    ANCH_AUTH_DOT_COMPANY = 'anch_auth.company'
    ANCH_AUTH_DOT_COMPANYROLE = 'anch_auth.companyrole'
    ANCH_AUTH_DOT_COMPANYROLE_PERMISSION_ENUM = 'anch_auth.companyrolePermissionEnum'
    ANCH_AUTH_DOT_USERLICENSE = 'anch_auth.userlicense'
    ANCH_AUTH_DOT_APIKEY = 'anch_auth.apikey'
    ANCH_AUTH_DOT_OAUTHTOKEN = 'anch_auth.oauthtoken'
    ANCH_AUTH_DOT_COMPANYCATEGORY = 'anch_auth.companycategory'
    ANCH_CORP_DOT_DEPARTMENT = 'anch_corp.department'
    ANCH_CORP_DOT_EMPLOYEE = 'anch_corp.employee'
    ANCH_CORP_DOT_DEPARTMENTMEMBERSHIP = 'anch_corp.departmentmembership'
    ANCH_CORP_DOT_CONTRACT = 'anch_corp.contract'
    ANCH_CORP_DOT_DEPARTMENTCONTRACT = 'anch_corp.departmentcontract'
    ANCH_CORP_DOT_CONTRACTTOOL = 'anch_corp.contracttool'
    ANCH_CORP_DOT_CONTRACTTOOLTRANSACTION = 'anch_corp.contracttooltransaction'
    ANCH_TOOLS_DOT_TOOL = 'anch_tools.tool'
    ANCH_TOOLS_DOT_TOOLCATEGORY = 'anch_tools.toolcategory'
    ANCH_TOOLS_DOT_TOOLACCESS = 'anch_tools.toolaccess'
    ANCH_TOOLS_DOT_TAGTHOUGH = 'anch_tools.tagthough'
    ANCH_CORP_DOT_BANKACCOUNT = 'anch_corp.bankaccount'
    ANCH_CORP_DOT_TRANSACTION = 'anch_corp.transaction'
    ANCH_METERING_DOT_METEREDSERVICE = 'anch_metering.meteredservice'
    ANCH_METERING_DOT_METEREDALERT = 'anch_metering.meteredalert'
    ANCH_METERING_DOT_METERENTRY = 'anch_metering.meterentry'
    ANCH_NOTIFICATION_DOT_NOTIFICATION = 'anch_notification.notification'
    TAGGIT_DOT_TAG = 'taggit.tag'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ContentTypeNaturalKey from a JSON string"""
        return cls(json.loads(json_str))


