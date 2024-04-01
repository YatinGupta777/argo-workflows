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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from argo_workflows.models.io_argoproj_events_v1alpha1_event_source_filter import IoArgoprojEventsV1alpha1EventSourceFilter
from argo_workflows.models.io_argoproj_events_v1alpha1_webhook_context import IoArgoprojEventsV1alpha1WebhookContext
from typing import Optional, Set
from typing_extensions import Self

class IoArgoprojEventsV1alpha1WebhookEventSource(BaseModel):
    """
    IoArgoprojEventsV1alpha1WebhookEventSource
    """ # noqa: E501
    filter: Optional[IoArgoprojEventsV1alpha1EventSourceFilter] = None
    webhook_context: Optional[IoArgoprojEventsV1alpha1WebhookContext] = Field(default=None, alias="webhookContext")
    __properties: ClassVar[List[str]] = ["filter", "webhookContext"]

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
        """Create an instance of IoArgoprojEventsV1alpha1WebhookEventSource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of webhook_context
        if self.webhook_context:
            _dict['webhookContext'] = self.webhook_context.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoArgoprojEventsV1alpha1WebhookEventSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "filter": IoArgoprojEventsV1alpha1EventSourceFilter.from_dict(obj["filter"]) if obj.get("filter") is not None else None,
            "webhookContext": IoArgoprojEventsV1alpha1WebhookContext.from_dict(obj["webhookContext"]) if obj.get("webhookContext") is not None else None
        })
        return _obj


