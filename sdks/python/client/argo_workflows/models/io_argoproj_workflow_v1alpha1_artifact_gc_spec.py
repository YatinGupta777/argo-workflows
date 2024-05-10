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
from argo_workflows.models.io_argoproj_workflow_v1alpha1_artifact_node_spec import IoArgoprojWorkflowV1alpha1ArtifactNodeSpec
from typing import Optional, Set
from typing_extensions import Self

class IoArgoprojWorkflowV1alpha1ArtifactGCSpec(BaseModel):
    """
    ArtifactGCSpec specifies the Artifacts that need to be deleted
    """ # noqa: E501
    artifacts_by_node: Optional[Dict[str, IoArgoprojWorkflowV1alpha1ArtifactNodeSpec]] = Field(default=None, description="ArtifactsByNode maps Node name to information pertaining to Artifacts on that Node", alias="artifactsByNode")
    __properties: ClassVar[List[str]] = ["artifactsByNode"]

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
        """Create an instance of IoArgoprojWorkflowV1alpha1ArtifactGCSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in artifacts_by_node (dict)
        _field_dict = {}
        if self.artifacts_by_node:
            for _key in self.artifacts_by_node:
                if self.artifacts_by_node[_key]:
                    _field_dict[_key] = self.artifacts_by_node[_key].to_dict()
            _dict['artifactsByNode'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoArgoprojWorkflowV1alpha1ArtifactGCSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "artifactsByNode": dict(
                (_k, IoArgoprojWorkflowV1alpha1ArtifactNodeSpec.from_dict(_v))
                for _k, _v in obj["artifactsByNode"].items()
            )
            if obj.get("artifactsByNode") is not None
            else None
        })
        return _obj


