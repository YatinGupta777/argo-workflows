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
from argo_workflows.models.io_argoproj_events_v1alpha1_basic_auth import IoArgoprojEventsV1alpha1BasicAuth
from argo_workflows.models.io_argoproj_events_v1alpha1_secure_header import IoArgoprojEventsV1alpha1SecureHeader
from argo_workflows.models.io_argoproj_events_v1alpha1_tls_config import IoArgoprojEventsV1alpha1TLSConfig
from argo_workflows.models.io_argoproj_events_v1alpha1_trigger_parameter import IoArgoprojEventsV1alpha1TriggerParameter
from typing import Optional, Set
from typing_extensions import Self

class IoArgoprojEventsV1alpha1HTTPTrigger(BaseModel):
    """
    IoArgoprojEventsV1alpha1HTTPTrigger
    """ # noqa: E501
    basic_auth: Optional[IoArgoprojEventsV1alpha1BasicAuth] = Field(default=None, alias="basicAuth")
    headers: Optional[Dict[str, StrictStr]] = None
    method: Optional[StrictStr] = None
    parameters: Optional[List[IoArgoprojEventsV1alpha1TriggerParameter]] = Field(default=None, description="Parameters is the list of key-value extracted from event's payload that are applied to the HTTP trigger resource.")
    payload: Optional[List[IoArgoprojEventsV1alpha1TriggerParameter]] = None
    secure_headers: Optional[List[IoArgoprojEventsV1alpha1SecureHeader]] = Field(default=None, alias="secureHeaders")
    timeout: Optional[StrictStr] = None
    tls: Optional[IoArgoprojEventsV1alpha1TLSConfig] = None
    url: Optional[StrictStr] = Field(default=None, description="URL refers to the URL to send HTTP request to.")
    __properties: ClassVar[List[str]] = ["basicAuth", "headers", "method", "parameters", "payload", "secureHeaders", "timeout", "tls", "url"]

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
        """Create an instance of IoArgoprojEventsV1alpha1HTTPTrigger from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of basic_auth
        if self.basic_auth:
            _dict['basicAuth'] = self.basic_auth.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of each item in secure_headers (list)
        _items = []
        if self.secure_headers:
            for _item in self.secure_headers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['secureHeaders'] = _items
        # override the default output from pydantic by calling `to_dict()` of tls
        if self.tls:
            _dict['tls'] = self.tls.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoArgoprojEventsV1alpha1HTTPTrigger from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "basicAuth": IoArgoprojEventsV1alpha1BasicAuth.from_dict(obj["basicAuth"]) if obj.get("basicAuth") is not None else None,
            "headers": obj.get("headers"),
            "method": obj.get("method"),
            "parameters": [IoArgoprojEventsV1alpha1TriggerParameter.from_dict(_item) for _item in obj["parameters"]] if obj.get("parameters") is not None else None,
            "payload": [IoArgoprojEventsV1alpha1TriggerParameter.from_dict(_item) for _item in obj["payload"]] if obj.get("payload") is not None else None,
            "secureHeaders": [IoArgoprojEventsV1alpha1SecureHeader.from_dict(_item) for _item in obj["secureHeaders"]] if obj.get("secureHeaders") is not None else None,
            "timeout": obj.get("timeout"),
            "tls": IoArgoprojEventsV1alpha1TLSConfig.from_dict(obj["tls"]) if obj.get("tls") is not None else None,
            "url": obj.get("url")
        })
        return _obj

