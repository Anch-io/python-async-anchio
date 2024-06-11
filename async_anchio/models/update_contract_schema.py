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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from async_anchio.models.payment_frequency_enum import PaymentFrequencyEnum
from async_anchio.models.payment_terms_enum import PaymentTermsEnum
from async_anchio.models.renewal_policy_enum import RenewalPolicyEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UpdateContractSchema(BaseModel):
    """
    UpdateContractSchema
    """ # noqa: E501
    created_on: Optional[StrictStr] = None
    updated_on: Optional[StrictStr] = None
    id: StrictStr
    name: StrictStr
    department_ids: List[StrictStr]
    justification: StrictStr
    start: StrictStr
    end: Optional[StrictStr] = None
    signing_date: Optional[StrictStr] = None
    contract_amount: Optional[Union[StrictFloat, StrictInt]] = 0
    payment_terms: PaymentTermsEnum
    payment_frequency: PaymentFrequencyEnum
    notes: Optional[StrictStr] = ''
    agreement_link: Optional[StrictStr] = ''
    contract_signer: Optional[StrictStr] = None
    renewal_policy: RenewalPolicyEnum
    __properties: ClassVar[List[str]] = ["created_on", "updated_on", "id", "name", "department_ids", "justification", "start", "end", "signing_date", "contract_amount", "payment_terms", "payment_frequency", "notes", "agreement_link", "contract_signer", "renewal_policy"]

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
        """Create an instance of UpdateContractSchema from a JSON string"""
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
        """Create an instance of UpdateContractSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_on": obj.get("created_on"),
            "updated_on": obj.get("updated_on"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "department_ids": obj.get("department_ids"),
            "justification": obj.get("justification"),
            "start": obj.get("start"),
            "end": obj.get("end"),
            "signing_date": obj.get("signing_date"),
            "contract_amount": obj.get("contract_amount") if obj.get("contract_amount") is not None else 0,
            "payment_terms": obj.get("payment_terms"),
            "payment_frequency": obj.get("payment_frequency"),
            "notes": obj.get("notes") if obj.get("notes") is not None else '',
            "agreement_link": obj.get("agreement_link") if obj.get("agreement_link") is not None else '',
            "contract_signer": obj.get("contract_signer"),
            "renewal_policy": obj.get("renewal_policy")
        })
        return _obj


