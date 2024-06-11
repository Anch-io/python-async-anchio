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
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from async_anchio.models.scope_enum import ScopeEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class KeySchema(BaseModel):
    """
    KeySchema
    """ # noqa: E501
    created_on: Optional[StrictStr] = None
    updated_on: Optional[StrictStr] = None
    id: StrictStr
    name: StrictStr
    key: Optional[StrictStr] = None
    user_license: StrictStr
    last_used: Optional[StrictStr] = None
    scopes: Optional[List[ScopeEnum]] = None
    __properties: ClassVar[List[str]] = ["created_on", "updated_on", "id", "name", "key", "user_license", "last_used", "scopes"]

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
        """Create an instance of KeySchema from a JSON string"""
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
        # set to None if created_on (nullable) is None
        # and model_fields_set contains the field
        if self.created_on is None and "created_on" in self.model_fields_set:
            _dict['created_on'] = None

        # set to None if updated_on (nullable) is None
        # and model_fields_set contains the field
        if self.updated_on is None and "updated_on" in self.model_fields_set:
            _dict['updated_on'] = None

        # set to None if key (nullable) is None
        # and model_fields_set contains the field
        if self.key is None and "key" in self.model_fields_set:
            _dict['key'] = None

        # set to None if last_used (nullable) is None
        # and model_fields_set contains the field
        if self.last_used is None and "last_used" in self.model_fields_set:
            _dict['last_used'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of KeySchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_on": obj.get("created_on"),
            "updated_on": obj.get("updated_on"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "key": obj.get("key"),
            "user_license": obj.get("user_license"),
            "last_used": obj.get("last_used"),
            "scopes": obj.get("scopes")
        })
        return _obj


