"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from datetime import datetime
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class UploadSessionTypedDict(TypedDict):
    id: NotRequired[str]
    r"""A unique identifier for an object."""
    success: NotRequired[bool]
    r"""Indicates if the upload session was completed successfully."""
    part_size: NotRequired[float]
    r"""Size in bytes of each part of the file that you will upload. Uploaded parts need to be this size for the upload to be successful."""
    parallel_upload_supported: NotRequired[bool]
    r"""Indicates if parts of the file can uploaded in parallel."""
    uploaded_byte_range: NotRequired[str]
    r"""The range of bytes that was successfully uploaded."""
    expires_at: NotRequired[Nullable[datetime]]


class UploadSession(BaseModel):
    id: Optional[str] = None
    r"""A unique identifier for an object."""

    success: Optional[bool] = None
    r"""Indicates if the upload session was completed successfully."""

    part_size: Optional[float] = None
    r"""Size in bytes of each part of the file that you will upload. Uploaded parts need to be this size for the upload to be successful."""

    parallel_upload_supported: Optional[bool] = None
    r"""Indicates if parts of the file can uploaded in parallel."""

    uploaded_byte_range: Optional[str] = None
    r"""The range of bytes that was successfully uploaded."""

    expires_at: OptionalNullable[datetime] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "success",
            "part_size",
            "parallel_upload_supported",
            "uploaded_byte_range",
            "expires_at",
        ]
        nullable_fields = ["expires_at"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
