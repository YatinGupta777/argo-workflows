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
from argo_workflows.models.io_argoproj_workflow_v1alpha1_backoff import IoArgoprojWorkflowV1alpha1Backoff
from argo_workflows.models.io_argoproj_workflow_v1alpha1_retry_affinity import IoArgoprojWorkflowV1alpha1RetryAffinity
from typing import Optional, Set
from typing_extensions import Self

class IoArgoprojWorkflowV1alpha1RetryStrategy(BaseModel):
    """
    RetryStrategy provides controls on how to retry a workflow step
    """ # noqa: E501
    affinity: Optional[IoArgoprojWorkflowV1alpha1RetryAffinity] = None
    backoff: Optional[IoArgoprojWorkflowV1alpha1Backoff] = None
    expression: Optional[StrictStr] = Field(default=None, description="Expression is a condition expression for when a node will be retried. If it evaluates to false, the node will not be retried and the retry strategy will be ignored")
    limit: Optional[StrictStr] = None
    retry_policy: Optional[StrictStr] = Field(default=None, description="RetryPolicy is a policy of NodePhase statuses that will be retried", alias="retryPolicy")
    __properties: ClassVar[List[str]] = ["affinity", "backoff", "expression", "limit", "retryPolicy"]

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
        """Create an instance of IoArgoprojWorkflowV1alpha1RetryStrategy from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of affinity
        if self.affinity:
            _dict['affinity'] = self.affinity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of backoff
        if self.backoff:
            _dict['backoff'] = self.backoff.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoArgoprojWorkflowV1alpha1RetryStrategy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "affinity": IoArgoprojWorkflowV1alpha1RetryAffinity.from_dict(obj["affinity"]) if obj.get("affinity") is not None else None,
            "backoff": IoArgoprojWorkflowV1alpha1Backoff.from_dict(obj["backoff"]) if obj.get("backoff") is not None else None,
            "expression": obj.get("expression"),
            "limit": obj.get("limit"),
            "retryPolicy": obj.get("retryPolicy")
        })
        return _obj

