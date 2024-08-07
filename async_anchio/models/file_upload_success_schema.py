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
from pydantic import BaseModel, StrictInt
from async_anchio.models.failed_row_schema import FailedRowSchema
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FileUploadSuccessSchema(BaseModel):
    """
    FileUploadSuccessSchema
    """ # noqa: E501
    tool_accesses: Optional[StrictInt] = 0
    contracts: Optional[StrictInt] = 0
    contract_tools: Optional[StrictInt] = 0
    departments: Optional[StrictInt] = 0
    department_contracts: Optional[StrictInt] = 0
    department_memberships: Optional[StrictInt] = 0
    employees: Optional[StrictInt] = 0
    tools: Optional[StrictInt] = 0
    tool_categories: Optional[StrictInt] = 0
    failed_rows: List[FailedRowSchema]
    __properties: ClassVar[List[str]] = ["tool_accesses", "contracts", "contract_tools", "departments", "department_contracts", "department_memberships", "employees", "tools", "tool_categories", "failed_rows"]

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
        """Create an instance of FileUploadSuccessSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in failed_rows (list)
        _items = []
        if self.failed_rows:
            for _item in self.failed_rows:
                if _item:
                    _items.append(_item.to_dict())
            _dict['failed_rows'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FileUploadSuccessSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tool_accesses": obj.get("tool_accesses") if obj.get("tool_accesses") is not None else 0,
            "contracts": obj.get("contracts") if obj.get("contracts") is not None else 0,
            "contract_tools": obj.get("contract_tools") if obj.get("contract_tools") is not None else 0,
            "departments": obj.get("departments") if obj.get("departments") is not None else 0,
            "department_contracts": obj.get("department_contracts") if obj.get("department_contracts") is not None else 0,
            "department_memberships": obj.get("department_memberships") if obj.get("department_memberships") is not None else 0,
            "employees": obj.get("employees") if obj.get("employees") is not None else 0,
            "tools": obj.get("tools") if obj.get("tools") is not None else 0,
            "tool_categories": obj.get("tool_categories") if obj.get("tool_categories") is not None else 0,
            "failed_rows": [FailedRowSchema.from_dict(_item) for _item in obj.get("failed_rows")] if obj.get("failed_rows") is not None else None
        })
        return _obj


