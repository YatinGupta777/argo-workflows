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
from argo_workflows.models.config_map_env_source import ConfigMapEnvSource
from argo_workflows.models.secret_env_source import SecretEnvSource
from typing import Optional, Set
from typing_extensions import Self

class EnvFromSource(BaseModel):
    """
    EnvFromSource represents the source of a set of ConfigMaps
    """ # noqa: E501
    config_map_ref: Optional[ConfigMapEnvSource] = Field(default=None, alias="configMapRef")
    prefix: Optional[StrictStr] = Field(default=None, description="An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER.")
    secret_ref: Optional[SecretEnvSource] = Field(default=None, alias="secretRef")
    __properties: ClassVar[List[str]] = ["configMapRef", "prefix", "secretRef"]

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
        """Create an instance of EnvFromSource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of config_map_ref
        if self.config_map_ref:
            _dict['configMapRef'] = self.config_map_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secret_ref
        if self.secret_ref:
            _dict['secretRef'] = self.secret_ref.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EnvFromSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "configMapRef": ConfigMapEnvSource.from_dict(obj["configMapRef"]) if obj.get("configMapRef") is not None else None,
            "prefix": obj.get("prefix"),
            "secretRef": SecretEnvSource.from_dict(obj["secretRef"]) if obj.get("secretRef") is not None else None
        })
        return _obj


