# coding: utf-8

"""
    Anch.io

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.6
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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CompanySchema(BaseModel):
    """
    CompanySchema
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="id")
    allowed_origins: Optional[List[StrictStr]] = None
    has_customer: Optional[StrictBool] = False
    is_trial_active: Optional[StrictBool] = False
    is_subscription_active: Optional[StrictBool] = False
    employee_count: Optional[StrictInt] = 0
    name: Annotated[str, Field(strict=True, max_length=255)] = Field(description="name")
    handle: Annotated[str, Field(strict=True, max_length=128)] = Field(description="handle")
    keycloak_group: Optional[StrictStr] = None
    description: Optional[StrictStr] = Field(default='', description="description")
    logo: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    category: Optional[StrictStr] = None
    address_1: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = Field(default='', description="address_1")
    address_2: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = Field(default='', description="address_2")
    city: Optional[Annotated[str, Field(strict=True, max_length=256)]] = Field(default='', description="city")
    state: Optional[Annotated[str, Field(strict=True, max_length=128)]] = Field(default='', description="state")
    country: StrictStr
    postal_code: Optional[Annotated[str, Field(strict=True, max_length=32)]] = Field(default='', description="postal_code")
    last_employee_sync: Optional[datetime] = None
    last_find_employee_app_sync: Optional[datetime] = None
    slug: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="slug")
    __properties: ClassVar[List[str]] = ["id", "allowed_origins", "has_customer", "is_trial_active", "is_subscription_active", "employee_count", "name", "handle", "keycloak_group", "description", "logo", "email", "phone", "category", "address_1", "address_2", "city", "state", "country", "postal_code", "last_employee_sync", "last_find_employee_app_sync", "slug"]

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
        """Create an instance of CompanySchema from a JSON string"""
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
        # set to None if keycloak_group (nullable) is None
        # and model_fields_set contains the field
        if self.keycloak_group is None and "keycloak_group" in self.model_fields_set:
            _dict['keycloak_group'] = None

        # set to None if logo (nullable) is None
        # and model_fields_set contains the field
        if self.logo is None and "logo" in self.model_fields_set:
            _dict['logo'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if phone (nullable) is None
        # and model_fields_set contains the field
        if self.phone is None and "phone" in self.model_fields_set:
            _dict['phone'] = None

        # set to None if category (nullable) is None
        # and model_fields_set contains the field
        if self.category is None and "category" in self.model_fields_set:
            _dict['category'] = None

        # set to None if last_employee_sync (nullable) is None
        # and model_fields_set contains the field
        if self.last_employee_sync is None and "last_employee_sync" in self.model_fields_set:
            _dict['last_employee_sync'] = None

        # set to None if last_find_employee_app_sync (nullable) is None
        # and model_fields_set contains the field
        if self.last_find_employee_app_sync is None and "last_find_employee_app_sync" in self.model_fields_set:
            _dict['last_find_employee_app_sync'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CompanySchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "allowed_origins": obj.get("allowed_origins"),
            "has_customer": obj.get("has_customer") if obj.get("has_customer") is not None else False,
            "is_trial_active": obj.get("is_trial_active") if obj.get("is_trial_active") is not None else False,
            "is_subscription_active": obj.get("is_subscription_active") if obj.get("is_subscription_active") is not None else False,
            "employee_count": obj.get("employee_count") if obj.get("employee_count") is not None else 0,
            "name": obj.get("name"),
            "handle": obj.get("handle"),
            "keycloak_group": obj.get("keycloak_group"),
            "description": obj.get("description") if obj.get("description") is not None else '',
            "logo": obj.get("logo"),
            "email": obj.get("email"),
            "phone": obj.get("phone"),
            "category": obj.get("category"),
            "address_1": obj.get("address_1") if obj.get("address_1") is not None else '',
            "address_2": obj.get("address_2") if obj.get("address_2") is not None else '',
            "city": obj.get("city") if obj.get("city") is not None else '',
            "state": obj.get("state") if obj.get("state") is not None else '',
            "country": obj.get("country"),
            "postal_code": obj.get("postal_code") if obj.get("postal_code") is not None else '',
            "last_employee_sync": obj.get("last_employee_sync"),
            "last_find_employee_app_sync": obj.get("last_find_employee_app_sync"),
            "slug": obj.get("slug")
        })
        return _obj


