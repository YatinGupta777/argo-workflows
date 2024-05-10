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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from argo_workflows.models.managed_fields_entry import ManagedFieldsEntry
from argo_workflows.models.owner_reference import OwnerReference
from typing import Optional, Set
from typing_extensions import Self

class ObjectMeta(BaseModel):
    """
    ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create.
    """ # noqa: E501
    annotations: Optional[Dict[str, StrictStr]] = Field(default=None, description="Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations")
    cluster_name: Optional[StrictStr] = Field(default=None, description="The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.", alias="clusterName")
    creation_timestamp: Optional[datetime] = Field(default=None, description="Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.", alias="creationTimestamp")
    deletion_grace_period_seconds: Optional[StrictInt] = Field(default=None, description="Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.", alias="deletionGracePeriodSeconds")
    deletion_timestamp: Optional[datetime] = Field(default=None, description="Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.", alias="deletionTimestamp")
    finalizers: Optional[List[StrictStr]] = Field(default=None, description="Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order.  Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.")
    generate_name: Optional[StrictStr] = Field(default=None, description="GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.  If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).  Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency", alias="generateName")
    generation: Optional[StrictInt] = Field(default=None, description="A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.")
    labels: Optional[Dict[str, StrictStr]] = Field(default=None, description="Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels")
    managed_fields: Optional[List[ManagedFieldsEntry]] = Field(default=None, description="ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object.", alias="managedFields")
    name: Optional[StrictStr] = Field(default=None, description="Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names")
    namespace: Optional[StrictStr] = Field(default=None, description="Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.  Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces")
    owner_references: Optional[List[OwnerReference]] = Field(default=None, description="List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.", alias="ownerReferences")
    resource_version: Optional[StrictStr] = Field(default=None, description="An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.  Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency", alias="resourceVersion")
    self_link: Optional[StrictStr] = Field(default=None, description="SelfLink is a URL representing this object. Populated by the system. Read-only.  DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.", alias="selfLink")
    uid: Optional[StrictStr] = Field(default=None, description="UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.  Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids")
    __properties: ClassVar[List[str]] = ["annotations", "clusterName", "creationTimestamp", "deletionGracePeriodSeconds", "deletionTimestamp", "finalizers", "generateName", "generation", "labels", "managedFields", "name", "namespace", "ownerReferences", "resourceVersion", "selfLink", "uid"]

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
        """Create an instance of ObjectMeta from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in managed_fields (list)
        _items = []
        if self.managed_fields:
            for _item in self.managed_fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['managedFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in owner_references (list)
        _items = []
        if self.owner_references:
            for _item in self.owner_references:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ownerReferences'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObjectMeta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "annotations": obj.get("annotations"),
            "clusterName": obj.get("clusterName"),
            "creationTimestamp": obj.get("creationTimestamp"),
            "deletionGracePeriodSeconds": obj.get("deletionGracePeriodSeconds"),
            "deletionTimestamp": obj.get("deletionTimestamp"),
            "finalizers": obj.get("finalizers"),
            "generateName": obj.get("generateName"),
            "generation": obj.get("generation"),
            "labels": obj.get("labels"),
            "managedFields": [ManagedFieldsEntry.from_dict(_item) for _item in obj["managedFields"]] if obj.get("managedFields") is not None else None,
            "name": obj.get("name"),
            "namespace": obj.get("namespace"),
            "ownerReferences": [OwnerReference.from_dict(_item) for _item in obj["ownerReferences"]] if obj.get("ownerReferences") is not None else None,
            "resourceVersion": obj.get("resourceVersion"),
            "selfLink": obj.get("selfLink"),
            "uid": obj.get("uid")
        })
        return _obj


