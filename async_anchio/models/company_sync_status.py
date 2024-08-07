# coding: utf-8

"""
    Anch.io

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.9
    Contact: opensource@anchio.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from async_anchio.models.sync_status import SyncStatus
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CompanySyncStatus(BaseModel):
    """
    CompanySyncStatus
    """ # noqa: E501
    employee_sync: Optional[SyncStatus] = None
    find_employee_app_sync: Optional[SyncStatus] = None
    activity_sync: Optional[SyncStatus] = None
    plaid_sync: Optional[SyncStatus] = None
    lang_smith_sync: Optional[SyncStatus] = None
    __properties: ClassVar[List[str]] = ["employee_sync", "find_employee_app_sync", "activity_sync", "plaid_sync", "lang_smith_sync"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CompanySyncStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of employee_sync
        if self.employee_sync:
            _dict['employee_sync'] = self.employee_sync.to_dict()
        # override the default output from pydantic by calling `to_dict()` of find_employee_app_sync
        if self.find_employee_app_sync:
            _dict['find_employee_app_sync'] = self.find_employee_app_sync.to_dict()
        # override the default output from pydantic by calling `to_dict()` of activity_sync
        if self.activity_sync:
            _dict['activity_sync'] = self.activity_sync.to_dict()
        # override the default output from pydantic by calling `to_dict()` of plaid_sync
        if self.plaid_sync:
            _dict['plaid_sync'] = self.plaid_sync.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lang_smith_sync
        if self.lang_smith_sync:
            _dict['lang_smith_sync'] = self.lang_smith_sync.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CompanySyncStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "employee_sync": SyncStatus.from_dict(obj.get("employee_sync")) if obj.get("employee_sync") is not None else None,
            "find_employee_app_sync": SyncStatus.from_dict(obj.get("find_employee_app_sync")) if obj.get("find_employee_app_sync") is not None else None,
            "activity_sync": SyncStatus.from_dict(obj.get("activity_sync")) if obj.get("activity_sync") is not None else None,
            "plaid_sync": SyncStatus.from_dict(obj.get("plaid_sync")) if obj.get("plaid_sync") is not None else None,
            "lang_smith_sync": SyncStatus.from_dict(obj.get("lang_smith_sync")) if obj.get("lang_smith_sync") is not None else None
        })
        return _obj


