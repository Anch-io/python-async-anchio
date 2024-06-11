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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from async_anchio.models.permission_enum import PermissionEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UserLicenseSchema(BaseModel):
    """
    UserLicenseSchema
    """ # noqa: E501
    id: StrictStr
    created_on: Optional[datetime] = Field(default=None, description="created_on")
    updated_on: Optional[datetime] = Field(default=None, description="updated_on")
    user: Optional[StrictStr] = None
    company: StrictStr
    handle: Optional[StrictStr] = None
    avatar: Optional[StrictStr] = None
    email: StrictStr
    onboarding_complete: Optional[StrictBool] = False
    roles: List[StrictStr]
    permissions: List[PermissionEnum]
    __properties: ClassVar[List[str]] = ["id", "created_on", "updated_on", "user", "company", "handle", "avatar", "email", "onboarding_complete", "roles", "permissions"]

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
        """Create an instance of UserLicenseSchema from a JSON string"""
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
        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        # set to None if handle (nullable) is None
        # and model_fields_set contains the field
        if self.handle is None and "handle" in self.model_fields_set:
            _dict['handle'] = None

        # set to None if avatar (nullable) is None
        # and model_fields_set contains the field
        if self.avatar is None and "avatar" in self.model_fields_set:
            _dict['avatar'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UserLicenseSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_on": obj.get("created_on"),
            "updated_on": obj.get("updated_on"),
            "user": obj.get("user"),
            "company": obj.get("company"),
            "handle": obj.get("handle"),
            "avatar": obj.get("avatar"),
            "email": obj.get("email"),
            "onboarding_complete": obj.get("onboarding_complete") if obj.get("onboarding_complete") is not None else False,
            "roles": obj.get("roles"),
            "permissions": obj.get("permissions")
        })
        return _obj


