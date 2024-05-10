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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from argo_workflows.models.io_argoproj_events_v1alpha1_trigger_parameter import IoArgoprojEventsV1alpha1TriggerParameter
from argo_workflows.models.secret_key_selector import SecretKeySelector
from typing import Optional, Set
from typing_extensions import Self

class IoArgoprojEventsV1alpha1OpenWhiskTrigger(BaseModel):
    """
    OpenWhiskTrigger refers to the specification of the OpenWhisk trigger.
    """ # noqa: E501
    action_name: Optional[StrictStr] = Field(default=None, description="Name of the action/function.", alias="actionName")
    auth_token: Optional[SecretKeySelector] = Field(default=None, alias="authToken")
    host: Optional[StrictStr] = Field(default=None, description="Host URL of the OpenWhisk.")
    namespace: Optional[StrictStr] = Field(default=None, description="Namespace for the action. Defaults to \"_\". +optional.")
    parameters: Optional[List[IoArgoprojEventsV1alpha1TriggerParameter]] = None
    payload: Optional[List[IoArgoprojEventsV1alpha1TriggerParameter]] = Field(default=None, description="Payload is the list of key-value extracted from an event payload to construct the request payload.")
    version: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["actionName", "authToken", "host", "namespace", "parameters", "payload", "version"]

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
        """Create an instance of IoArgoprojEventsV1alpha1OpenWhiskTrigger from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of auth_token
        if self.auth_token:
            _dict['authToken'] = self.auth_token.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in parameters (list)
        _items = []
        if self.parameters:
            for _item in self.parameters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parameters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in payload (list)
        _items = []
        if self.payload:
            for _item in self.payload:
                if _item:
                    _items.append(_item.to_dict())
            _dict['payload'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoArgoprojEventsV1alpha1OpenWhiskTrigger from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actionName": obj.get("actionName"),
            "authToken": SecretKeySelector.from_dict(obj["authToken"]) if obj.get("authToken") is not None else None,
            "host": obj.get("host"),
            "namespace": obj.get("namespace"),
            "parameters": [IoArgoprojEventsV1alpha1TriggerParameter.from_dict(_item) for _item in obj["parameters"]] if obj.get("parameters") is not None else None,
            "payload": [IoArgoprojEventsV1alpha1TriggerParameter.from_dict(_item) for _item in obj["payload"]] if obj.get("payload") is not None else None,
            "version": obj.get("version")
        })
        return _obj

