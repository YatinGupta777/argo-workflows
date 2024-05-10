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
from argo_workflows.models.io_argoproj_events_v1alpha1_watch_path_config import IoArgoprojEventsV1alpha1WatchPathConfig
from typing import Optional, Set
from typing_extensions import Self

class IoArgoprojEventsV1alpha1FileEventSource(BaseModel):
    """
    FileEventSource describes an event-source for file related events.
    """ # noqa: E501
    event_type: Optional[StrictStr] = Field(default=None, alias="eventType")
    filter: Optional[IoArgoprojEventsV1alpha1EventSourceFilter] = None
    metadata: Optional[Dict[str, StrictStr]] = None
    polling: Optional[StrictBool] = None
    watch_path_config: Optional[IoArgoprojEventsV1alpha1WatchPathConfig] = Field(default=None, alias="watchPathConfig")
    __properties: ClassVar[List[str]] = ["eventType", "filter", "metadata", "polling", "watchPathConfig"]

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
        """Create an instance of IoArgoprojEventsV1alpha1FileEventSource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of watch_path_config
        if self.watch_path_config:
            _dict['watchPathConfig'] = self.watch_path_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoArgoprojEventsV1alpha1FileEventSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "eventType": obj.get("eventType"),
            "filter": IoArgoprojEventsV1alpha1EventSourceFilter.from_dict(obj["filter"]) if obj.get("filter") is not None else None,
            "metadata": obj.get("metadata"),
            "polling": obj.get("polling"),
            "watchPathConfig": IoArgoprojEventsV1alpha1WatchPathConfig.from_dict(obj["watchPathConfig"]) if obj.get("watchPathConfig") is not None else None
        })
        return _obj

