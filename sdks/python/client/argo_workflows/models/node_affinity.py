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
from argo_workflows.models.node_selector import NodeSelector
from argo_workflows.models.preferred_scheduling_term import PreferredSchedulingTerm
from typing import Optional, Set
from typing_extensions import Self

class NodeAffinity(BaseModel):
    """
    Node affinity is a group of node affinity scheduling rules.
    """ # noqa: E501
    preferred_during_scheduling_ignored_during_execution: Optional[List[PreferredSchedulingTerm]] = Field(default=None, description="The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding \"weight\" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.", alias="preferredDuringSchedulingIgnoredDuringExecution")
    required_during_scheduling_ignored_during_execution: Optional[NodeSelector] = Field(default=None, alias="requiredDuringSchedulingIgnoredDuringExecution")
    __properties: ClassVar[List[str]] = ["preferredDuringSchedulingIgnoredDuringExecution", "requiredDuringSchedulingIgnoredDuringExecution"]

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
        """Create an instance of NodeAffinity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in preferred_during_scheduling_ignored_during_execution (list)
        _items = []
        if self.preferred_during_scheduling_ignored_during_execution:
            for _item in self.preferred_during_scheduling_ignored_during_execution:
                if _item:
                    _items.append(_item.to_dict())
            _dict['preferredDuringSchedulingIgnoredDuringExecution'] = _items
        # override the default output from pydantic by calling `to_dict()` of required_during_scheduling_ignored_during_execution
        if self.required_during_scheduling_ignored_during_execution:
            _dict['requiredDuringSchedulingIgnoredDuringExecution'] = self.required_during_scheduling_ignored_during_execution.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NodeAffinity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "preferredDuringSchedulingIgnoredDuringExecution": [PreferredSchedulingTerm.from_dict(_item) for _item in obj["preferredDuringSchedulingIgnoredDuringExecution"]] if obj.get("preferredDuringSchedulingIgnoredDuringExecution") is not None else None,
            "requiredDuringSchedulingIgnoredDuringExecution": NodeSelector.from_dict(obj["requiredDuringSchedulingIgnoredDuringExecution"]) if obj.get("requiredDuringSchedulingIgnoredDuringExecution") is not None else None
        })
        return _obj

