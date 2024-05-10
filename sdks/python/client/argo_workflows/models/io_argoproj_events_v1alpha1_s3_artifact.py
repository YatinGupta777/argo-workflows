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
from argo_workflows.models.io_argoproj_events_v1alpha1_s3_bucket import IoArgoprojEventsV1alpha1S3Bucket
from argo_workflows.models.io_argoproj_events_v1alpha1_s3_filter import IoArgoprojEventsV1alpha1S3Filter
from argo_workflows.models.secret_key_selector import SecretKeySelector
from typing import Optional, Set
from typing_extensions import Self

class IoArgoprojEventsV1alpha1S3Artifact(BaseModel):
    """
    IoArgoprojEventsV1alpha1S3Artifact
    """ # noqa: E501
    access_key: Optional[SecretKeySelector] = Field(default=None, alias="accessKey")
    bucket: Optional[IoArgoprojEventsV1alpha1S3Bucket] = None
    ca_certificate: Optional[SecretKeySelector] = Field(default=None, alias="caCertificate")
    endpoint: Optional[StrictStr] = None
    events: Optional[List[StrictStr]] = None
    filter: Optional[IoArgoprojEventsV1alpha1S3Filter] = None
    insecure: Optional[StrictBool] = None
    metadata: Optional[Dict[str, StrictStr]] = None
    region: Optional[StrictStr] = None
    secret_key: Optional[SecretKeySelector] = Field(default=None, alias="secretKey")
    __properties: ClassVar[List[str]] = ["accessKey", "bucket", "caCertificate", "endpoint", "events", "filter", "insecure", "metadata", "region", "secretKey"]

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
        """Create an instance of IoArgoprojEventsV1alpha1S3Artifact from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of access_key
        if self.access_key:
            _dict['accessKey'] = self.access_key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bucket
        if self.bucket:
            _dict['bucket'] = self.bucket.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ca_certificate
        if self.ca_certificate:
            _dict['caCertificate'] = self.ca_certificate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secret_key
        if self.secret_key:
            _dict['secretKey'] = self.secret_key.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoArgoprojEventsV1alpha1S3Artifact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessKey": SecretKeySelector.from_dict(obj["accessKey"]) if obj.get("accessKey") is not None else None,
            "bucket": IoArgoprojEventsV1alpha1S3Bucket.from_dict(obj["bucket"]) if obj.get("bucket") is not None else None,
            "caCertificate": SecretKeySelector.from_dict(obj["caCertificate"]) if obj.get("caCertificate") is not None else None,
            "endpoint": obj.get("endpoint"),
            "events": obj.get("events"),
            "filter": IoArgoprojEventsV1alpha1S3Filter.from_dict(obj["filter"]) if obj.get("filter") is not None else None,
            "insecure": obj.get("insecure"),
            "metadata": obj.get("metadata"),
            "region": obj.get("region"),
            "secretKey": SecretKeySelector.from_dict(obj["secretKey"]) if obj.get("secretKey") is not None else None
        })
        return _obj

