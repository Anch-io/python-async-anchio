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
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from async_anchio.models.employee_schema import EmployeeSchema
from async_anchio.models.payment_frequency_enum import PaymentFrequencyEnum
from async_anchio.models.payment_terms_enum import PaymentTermsEnum
from async_anchio.models.renewal_policy_enum import RenewalPolicyEnum
from async_anchio.models.tool_contract_schema import ToolContractSchema
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ContractSchema(BaseModel):
    """
    ContractSchema
    """ # noqa: E501
    id: StrictStr
    created_on: Optional[StrictStr] = None
    updated_on: Optional[StrictStr] = None
    department_ids: List[StrictStr]
    contract_tools: List[ToolContractSchema]
    name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default='', description="name")
    start: StrictStr
    end: Optional[StrictStr] = None
    signing_date: Optional[StrictStr] = None
    contract_amount: Optional[Union[StrictFloat, StrictInt]] = 0
    payment_terms: PaymentTermsEnum
    payment_frequency: PaymentFrequencyEnum
    justification: StrictStr
    notes: Optional[StrictStr] = ''
    agreement_link: Optional[StrictStr] = ''
    renewal_policy: RenewalPolicyEnum
    contract_signer: Optional[EmployeeSchema] = None
    user_count: Optional[StrictInt] = 0
    __properties: ClassVar[List[str]] = ["id", "created_on", "updated_on", "department_ids", "contract_tools", "name", "start", "end", "signing_date", "contract_amount", "payment_terms", "payment_frequency", "justification", "notes", "agreement_link", "renewal_policy", "contract_signer", "user_count"]

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
        """Create an instance of ContractSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in contract_tools (list)
        _items = []
        if self.contract_tools:
            for _item in self.contract_tools:
                if _item:
                    _items.append(_item.to_dict())
            _dict['contract_tools'] = _items
        # override the default output from pydantic by calling `to_dict()` of contract_signer
        if self.contract_signer:
            _dict['contract_signer'] = self.contract_signer.to_dict()
        # set to None if created_on (nullable) is None
        # and model_fields_set contains the field
        if self.created_on is None and "created_on" in self.model_fields_set:
            _dict['created_on'] = None

        # set to None if updated_on (nullable) is None
        # and model_fields_set contains the field
        if self.updated_on is None and "updated_on" in self.model_fields_set:
            _dict['updated_on'] = None

        # set to None if end (nullable) is None
        # and model_fields_set contains the field
        if self.end is None and "end" in self.model_fields_set:
            _dict['end'] = None

        # set to None if signing_date (nullable) is None
        # and model_fields_set contains the field
        if self.signing_date is None and "signing_date" in self.model_fields_set:
            _dict['signing_date'] = None

        # set to None if contract_signer (nullable) is None
        # and model_fields_set contains the field
        if self.contract_signer is None and "contract_signer" in self.model_fields_set:
            _dict['contract_signer'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ContractSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_on": obj.get("created_on"),
            "updated_on": obj.get("updated_on"),
            "department_ids": obj.get("department_ids"),
            "contract_tools": [ToolContractSchema.from_dict(_item) for _item in obj.get("contract_tools")] if obj.get("contract_tools") is not None else None,
            "name": obj.get("name") if obj.get("name") is not None else '',
            "start": obj.get("start"),
            "end": obj.get("end"),
            "signing_date": obj.get("signing_date"),
            "contract_amount": obj.get("contract_amount") if obj.get("contract_amount") is not None else 0,
            "payment_terms": obj.get("payment_terms"),
            "payment_frequency": obj.get("payment_frequency"),
            "justification": obj.get("justification"),
            "notes": obj.get("notes") if obj.get("notes") is not None else '',
            "agreement_link": obj.get("agreement_link") if obj.get("agreement_link") is not None else '',
            "renewal_policy": obj.get("renewal_policy"),
            "contract_signer": EmployeeSchema.from_dict(obj.get("contract_signer")) if obj.get("contract_signer") is not None else None,
            "user_count": obj.get("user_count") if obj.get("user_count") is not None else 0
        })
        return _obj


