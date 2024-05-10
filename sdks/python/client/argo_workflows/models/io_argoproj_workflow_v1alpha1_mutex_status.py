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
from argo_workflows.models.io_argoproj_workflow_v1alpha1_mutex_holding import IoArgoprojWorkflowV1alpha1MutexHolding
from typing import Optional, Set
from typing_extensions import Self

class IoArgoprojWorkflowV1alpha1MutexStatus(BaseModel):
    """
    MutexStatus contains which objects hold  mutex locks, and which objects this workflow is waiting on to release locks.
    """ # noqa: E501
    holding: Optional[List[IoArgoprojWorkflowV1alpha1MutexHolding]] = Field(default=None, description="Holding is a list of mutexes and their respective objects that are held by mutex lock for this io.argoproj.workflow.v1alpha1.")
    waiting: Optional[List[IoArgoprojWorkflowV1alpha1MutexHolding]] = Field(default=None, description="Waiting is a list of mutexes and their respective objects this workflow is waiting for.")
    __properties: ClassVar[List[str]] = ["holding", "waiting"]

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
        """Create an instance of IoArgoprojWorkflowV1alpha1MutexStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in holding (list)
        _items = []
        if self.holding:
            for _item in self.holding:
                if _item:
                    _items.append(_item.to_dict())
            _dict['holding'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in waiting (list)
        _items = []
        if self.waiting:
            for _item in self.waiting:
                if _item:
                    _items.append(_item.to_dict())
            _dict['waiting'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoArgoprojWorkflowV1alpha1MutexStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "holding": [IoArgoprojWorkflowV1alpha1MutexHolding.from_dict(_item) for _item in obj["holding"]] if obj.get("holding") is not None else None,
            "waiting": [IoArgoprojWorkflowV1alpha1MutexHolding.from_dict(_item) for _item in obj["waiting"]] if obj.get("waiting") is not None else None
        })
        return _obj

