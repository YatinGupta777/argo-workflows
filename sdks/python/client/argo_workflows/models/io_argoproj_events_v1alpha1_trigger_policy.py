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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from argo_workflows.models.io_argoproj_events_v1alpha1_k8_s_resource_policy import IoArgoprojEventsV1alpha1K8SResourcePolicy
from argo_workflows.models.io_argoproj_events_v1alpha1_status_policy import IoArgoprojEventsV1alpha1StatusPolicy
from typing import Optional, Set
from typing_extensions import Self

class IoArgoprojEventsV1alpha1TriggerPolicy(BaseModel):
    """
    IoArgoprojEventsV1alpha1TriggerPolicy
    """ # noqa: E501
    k8s: Optional[IoArgoprojEventsV1alpha1K8SResourcePolicy] = None
    status: Optional[IoArgoprojEventsV1alpha1StatusPolicy] = None
    __properties: ClassVar[List[str]] = ["k8s", "status"]

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
        """Create an instance of IoArgoprojEventsV1alpha1TriggerPolicy from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of k8s
        if self.k8s:
            _dict['k8s'] = self.k8s.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoArgoprojEventsV1alpha1TriggerPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "k8s": IoArgoprojEventsV1alpha1K8SResourcePolicy.from_dict(obj["k8s"]) if obj.get("k8s") is not None else None,
            "status": IoArgoprojEventsV1alpha1StatusPolicy.from_dict(obj["status"]) if obj.get("status") is not None else None
        })
        return _obj

