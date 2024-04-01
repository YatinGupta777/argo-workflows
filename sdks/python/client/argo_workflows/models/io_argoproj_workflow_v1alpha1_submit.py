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
from argo_workflows.models.io_argoproj_workflow_v1alpha1_arguments import IoArgoprojWorkflowV1alpha1Arguments
from argo_workflows.models.io_argoproj_workflow_v1alpha1_workflow_template_ref import IoArgoprojWorkflowV1alpha1WorkflowTemplateRef
from argo_workflows.models.object_meta import ObjectMeta
from typing import Optional, Set
from typing_extensions import Self

class IoArgoprojWorkflowV1alpha1Submit(BaseModel):
    """
    IoArgoprojWorkflowV1alpha1Submit
    """ # noqa: E501
    arguments: Optional[IoArgoprojWorkflowV1alpha1Arguments] = None
    metadata: Optional[ObjectMeta] = None
    workflow_template_ref: IoArgoprojWorkflowV1alpha1WorkflowTemplateRef = Field(alias="workflowTemplateRef")
    __properties: ClassVar[List[str]] = ["arguments", "metadata", "workflowTemplateRef"]

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
        """Create an instance of IoArgoprojWorkflowV1alpha1Submit from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of arguments
        if self.arguments:
            _dict['arguments'] = self.arguments.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of workflow_template_ref
        if self.workflow_template_ref:
            _dict['workflowTemplateRef'] = self.workflow_template_ref.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoArgoprojWorkflowV1alpha1Submit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "arguments": IoArgoprojWorkflowV1alpha1Arguments.from_dict(obj["arguments"]) if obj.get("arguments") is not None else None,
            "metadata": ObjectMeta.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "workflowTemplateRef": IoArgoprojWorkflowV1alpha1WorkflowTemplateRef.from_dict(obj["workflowTemplateRef"]) if obj.get("workflowTemplateRef") is not None else None
        })
        return _obj


