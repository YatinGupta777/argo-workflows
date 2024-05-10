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
from argo_workflows.models.io_argoproj_workflow_v1alpha1_arguments import IoArgoprojWorkflowV1alpha1Arguments
from argo_workflows.models.io_argoproj_workflow_v1alpha1_continue_on import IoArgoprojWorkflowV1alpha1ContinueOn
from argo_workflows.models.io_argoproj_workflow_v1alpha1_lifecycle_hook import IoArgoprojWorkflowV1alpha1LifecycleHook
from argo_workflows.models.io_argoproj_workflow_v1alpha1_sequence import IoArgoprojWorkflowV1alpha1Sequence
from argo_workflows.models.io_argoproj_workflow_v1alpha1_template import IoArgoprojWorkflowV1alpha1Template
from argo_workflows.models.io_argoproj_workflow_v1alpha1_template_ref import IoArgoprojWorkflowV1alpha1TemplateRef
from typing import Optional, Set
from typing_extensions import Self

class IoArgoprojWorkflowV1alpha1WorkflowStep(BaseModel):
    """
    WorkflowStep is a reference to a template to execute in a series of step
    """ # noqa: E501
    arguments: Optional[IoArgoprojWorkflowV1alpha1Arguments] = None
    continue_on: Optional[IoArgoprojWorkflowV1alpha1ContinueOn] = Field(default=None, alias="continueOn")
    hooks: Optional[Dict[str, IoArgoprojWorkflowV1alpha1LifecycleHook]] = Field(default=None, description="Hooks holds the lifecycle hook which is invoked at lifecycle of step, irrespective of the success, failure, or error status of the primary step")
    inline: Optional[IoArgoprojWorkflowV1alpha1Template] = None
    name: Optional[StrictStr] = Field(default=None, description="Name of the step")
    on_exit: Optional[StrictStr] = Field(default=None, description="OnExit is a template reference which is invoked at the end of the template, irrespective of the success, failure, or error of the primary template. DEPRECATED: Use Hooks[exit].Template instead.", alias="onExit")
    template: Optional[StrictStr] = Field(default=None, description="Template is the name of the template to execute as the step")
    template_ref: Optional[IoArgoprojWorkflowV1alpha1TemplateRef] = Field(default=None, alias="templateRef")
    when: Optional[StrictStr] = Field(default=None, description="When is an expression in which the step should conditionally execute")
    with_items: Optional[List[Dict[str, Any]]] = Field(default=None, description="WithItems expands a step into multiple parallel steps from the items in the list", alias="withItems")
    with_param: Optional[StrictStr] = Field(default=None, description="WithParam expands a step into multiple parallel steps from the value in the parameter, which is expected to be a JSON list.", alias="withParam")
    with_sequence: Optional[IoArgoprojWorkflowV1alpha1Sequence] = Field(default=None, alias="withSequence")
    __properties: ClassVar[List[str]] = ["arguments", "continueOn", "hooks", "inline", "name", "onExit", "template", "templateRef", "when", "withItems", "withParam", "withSequence"]

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
        """Create an instance of IoArgoprojWorkflowV1alpha1WorkflowStep from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of continue_on
        if self.continue_on:
            _dict['continueOn'] = self.continue_on.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in hooks (dict)
        _field_dict = {}
        if self.hooks:
            for _key in self.hooks:
                if self.hooks[_key]:
                    _field_dict[_key] = self.hooks[_key].to_dict()
            _dict['hooks'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of inline
        if self.inline:
            _dict['inline'] = self.inline.to_dict()
        # override the default output from pydantic by calling `to_dict()` of template_ref
        if self.template_ref:
            _dict['templateRef'] = self.template_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of with_sequence
        if self.with_sequence:
            _dict['withSequence'] = self.with_sequence.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoArgoprojWorkflowV1alpha1WorkflowStep from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "arguments": IoArgoprojWorkflowV1alpha1Arguments.from_dict(obj["arguments"]) if obj.get("arguments") is not None else None,
            "continueOn": IoArgoprojWorkflowV1alpha1ContinueOn.from_dict(obj["continueOn"]) if obj.get("continueOn") is not None else None,
            "hooks": dict(
                (_k, IoArgoprojWorkflowV1alpha1LifecycleHook.from_dict(_v))
                for _k, _v in obj["hooks"].items()
            )
            if obj.get("hooks") is not None
            else None,
            "inline": IoArgoprojWorkflowV1alpha1Template.from_dict(obj["inline"]) if obj.get("inline") is not None else None,
            "name": obj.get("name"),
            "onExit": obj.get("onExit"),
            "template": obj.get("template"),
            "templateRef": IoArgoprojWorkflowV1alpha1TemplateRef.from_dict(obj["templateRef"]) if obj.get("templateRef") is not None else None,
            "when": obj.get("when"),
            "withItems": obj.get("withItems"),
            "withParam": obj.get("withParam"),
            "withSequence": IoArgoprojWorkflowV1alpha1Sequence.from_dict(obj["withSequence"]) if obj.get("withSequence") is not None else None
        })
        return _obj

