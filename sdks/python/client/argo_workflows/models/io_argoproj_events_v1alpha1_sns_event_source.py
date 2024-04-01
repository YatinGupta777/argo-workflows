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
from argo_workflows.models.io_argoproj_events_v1alpha1_event_source_filter import IoArgoprojEventsV1alpha1EventSourceFilter
from argo_workflows.models.io_argoproj_events_v1alpha1_webhook_context import IoArgoprojEventsV1alpha1WebhookContext
from argo_workflows.models.secret_key_selector import SecretKeySelector
from typing import Optional, Set
from typing_extensions import Self

class IoArgoprojEventsV1alpha1SNSEventSource(BaseModel):
    """
    IoArgoprojEventsV1alpha1SNSEventSource
    """ # noqa: E501
    access_key: Optional[SecretKeySelector] = Field(default=None, alias="accessKey")
    endpoint: Optional[StrictStr] = None
    filter: Optional[IoArgoprojEventsV1alpha1EventSourceFilter] = None
    metadata: Optional[Dict[str, StrictStr]] = None
    region: Optional[StrictStr] = None
    role_arn: Optional[StrictStr] = Field(default=None, alias="roleARN")
    secret_key: Optional[SecretKeySelector] = Field(default=None, alias="secretKey")
    topic_arn: Optional[StrictStr] = Field(default=None, alias="topicArn")
    validate_signature: Optional[StrictBool] = Field(default=None, alias="validateSignature")
    webhook: Optional[IoArgoprojEventsV1alpha1WebhookContext] = None
    __properties: ClassVar[List[str]] = ["accessKey", "endpoint", "filter", "metadata", "region", "roleARN", "secretKey", "topicArn", "validateSignature", "webhook"]

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
        """Create an instance of IoArgoprojEventsV1alpha1SNSEventSource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of access_key
        if self.access_key:
            _dict['accessKey'] = self.access_key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secret_key
        if self.secret_key:
            _dict['secretKey'] = self.secret_key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of webhook
        if self.webhook:
            _dict['webhook'] = self.webhook.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoArgoprojEventsV1alpha1SNSEventSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessKey": SecretKeySelector.from_dict(obj["accessKey"]) if obj.get("accessKey") is not None else None,
            "endpoint": obj.get("endpoint"),
            "filter": IoArgoprojEventsV1alpha1EventSourceFilter.from_dict(obj["filter"]) if obj.get("filter") is not None else None,
            "metadata": obj.get("metadata"),
            "region": obj.get("region"),
            "roleARN": obj.get("roleARN"),
            "secretKey": SecretKeySelector.from_dict(obj["secretKey"]) if obj.get("secretKey") is not None else None,
            "topicArn": obj.get("topicArn"),
            "validateSignature": obj.get("validateSignature"),
            "webhook": IoArgoprojEventsV1alpha1WebhookContext.from_dict(obj["webhook"]) if obj.get("webhook") is not None else None
        })
        return _obj


