# coding: utf-8

"""
    Argo Workflows API

    Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argo-workflows.readthedocs.io/en/latest/

    The version of the OpenAPI document: VERSION
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class IoArgoprojWorkflowV1alpha1GetUserInfoResponse(BaseModel):
    """
    IoArgoprojWorkflowV1alpha1GetUserInfoResponse
    """ # noqa: E501
    email: Optional[StrictStr] = None
    email_verified: Optional[StrictBool] = Field(default=None, alias="emailVerified")
    groups: Optional[List[StrictStr]] = None
    issuer: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    service_account_name: Optional[StrictStr] = Field(default=None, alias="serviceAccountName")
    service_account_namespace: Optional[StrictStr] = Field(default=None, alias="serviceAccountNamespace")
    subject: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["email", "emailVerified", "groups", "issuer", "name", "serviceAccountName", "serviceAccountNamespace", "subject"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IoArgoprojWorkflowV1alpha1GetUserInfoResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoArgoprojWorkflowV1alpha1GetUserInfoResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email": obj.get("email"),
            "emailVerified": obj.get("emailVerified"),
            "groups": obj.get("groups"),
            "issuer": obj.get("issuer"),
            "name": obj.get("name"),
            "serviceAccountName": obj.get("serviceAccountName"),
            "serviceAccountNamespace": obj.get("serviceAccountNamespace"),
            "subject": obj.get("subject")
        })
        return _obj


