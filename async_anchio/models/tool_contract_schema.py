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
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from async_anchio.models.tool_category_schema import ToolCategorySchema
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ToolContractSchema(BaseModel):
    """
    ToolContractSchema
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="id")
    created_on: Optional[datetime] = Field(default=None, description="created_on")
    updated_on: Optional[datetime] = Field(default=None, description="updated_on")
    user_count: Optional[StrictInt] = None
    name: Annotated[str, Field(strict=True, max_length=512)] = Field(description="name")
    description: StrictStr = Field(description="description")
    logo: StrictStr = Field(description="logo")
    category: Optional[ToolCategorySchema] = None
    country: StrictStr
    has_subprocessor: Optional[StrictBool] = False
    hidden_date: Optional[datetime] = None
    tags: Optional[List[StrictStr]] = None
    seat_limit: Optional[StrictInt] = None
    tool_id: StrictStr
    contract_id: StrictStr
    __properties: ClassVar[List[str]] = ["id", "created_on", "updated_on", "user_count", "name", "description", "logo", "category", "country", "has_subprocessor", "hidden_date", "tags", "seat_limit", "tool_id", "contract_id"]

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
        """Create an instance of ToolContractSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of category
        if self.category:
            _dict['category'] = self.category.to_dict()
        # set to None if user_count (nullable) is None
        # and model_fields_set contains the field
        if self.user_count is None and "user_count" in self.model_fields_set:
            _dict['user_count'] = None

        # set to None if category (nullable) is None
        # and model_fields_set contains the field
        if self.category is None and "category" in self.model_fields_set:
            _dict['category'] = None

        # set to None if hidden_date (nullable) is None
        # and model_fields_set contains the field
        if self.hidden_date is None and "hidden_date" in self.model_fields_set:
            _dict['hidden_date'] = None

        # set to None if seat_limit (nullable) is None
        # and model_fields_set contains the field
        if self.seat_limit is None and "seat_limit" in self.model_fields_set:
            _dict['seat_limit'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ToolContractSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_on": obj.get("created_on"),
            "updated_on": obj.get("updated_on"),
            "user_count": obj.get("user_count"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "logo": obj.get("logo"),
            "category": ToolCategorySchema.from_dict(obj.get("category")) if obj.get("category") is not None else None,
            "country": obj.get("country"),
            "has_subprocessor": obj.get("has_subprocessor") if obj.get("has_subprocessor") is not None else False,
            "hidden_date": obj.get("hidden_date"),
            "tags": obj.get("tags"),
            "seat_limit": obj.get("seat_limit"),
            "tool_id": obj.get("tool_id"),
            "contract_id": obj.get("contract_id")
        })
        return _obj


