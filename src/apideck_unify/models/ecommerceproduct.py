"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .custommappings import CustomMappings, CustomMappingsTypedDict
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from datetime import datetime
from enum import Enum
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ProductStatus(str, Enum):
    r"""The current status of the product (active or archived)."""

    ACTIVE = "active"
    ARCHIVED = "archived"


class ImagesTypedDict(TypedDict):
    id: NotRequired[Nullable[str]]
    r"""A unique identifier for an object."""
    url: NotRequired[Nullable[str]]
    r"""The URL of an image of the product."""


class Images(BaseModel):
    id: OptionalNullable[str] = UNSET
    r"""A unique identifier for an object."""

    url: OptionalNullable[str] = UNSET
    r"""The URL of an image of the product."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "url"]
        nullable_fields = ["id", "url"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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


class EcommerceProductOptionsTypedDict(TypedDict):
    id: NotRequired[Nullable[str]]
    r"""A unique identifier for the option of the product."""
    name: NotRequired[Nullable[str]]
    r"""The name of the option for the product."""
    values: NotRequired[List[str]]


class EcommerceProductOptions(BaseModel):
    id: OptionalNullable[str] = UNSET
    r"""A unique identifier for the option of the product."""

    name: OptionalNullable[str] = UNSET
    r"""The name of the option for the product."""

    values: Optional[List[str]] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "name", "values"]
        nullable_fields = ["id", "name"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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


class EcommerceProductVariantsOptionsTypedDict(TypedDict):
    id: NotRequired[Nullable[str]]
    r"""A unique identifier for the option of the variant."""
    name: NotRequired[Nullable[str]]
    r"""The name of the option for the variant."""
    value: NotRequired[Nullable[str]]
    r"""The value of the option for the variant."""


class EcommerceProductVariantsOptions(BaseModel):
    id: OptionalNullable[str] = UNSET
    r"""A unique identifier for the option of the variant."""

    name: OptionalNullable[str] = UNSET
    r"""The name of the option for the variant."""

    value: OptionalNullable[str] = UNSET
    r"""The value of the option for the variant."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "name", "value"]
        nullable_fields = ["id", "name", "value"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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


class EcommerceProductImagesTypedDict(TypedDict):
    id: NotRequired[Nullable[str]]
    r"""A unique identifier for an object."""
    url: NotRequired[Nullable[str]]
    r"""The URL of an image of the variant."""


class EcommerceProductImages(BaseModel):
    id: OptionalNullable[str] = UNSET
    r"""A unique identifier for an object."""

    url: OptionalNullable[str] = UNSET
    r"""The URL of an image of the variant."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "url"]
        nullable_fields = ["id", "url"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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


class VariantsTypedDict(TypedDict):
    id: NotRequired[Nullable[str]]
    r"""A unique identifier for the variant of the product."""
    name: NotRequired[Nullable[str]]
    r"""The name for the variant, used for displaying to customers."""
    price: NotRequired[Nullable[str]]
    r"""The price of the variant."""
    sku: NotRequired[Nullable[str]]
    r"""The stock keeping unit of the variant."""
    inventory_quantity: NotRequired[Nullable[str]]
    r"""The quantity of the variant in stock."""
    weight: NotRequired[Nullable[str]]
    r"""The weight of the variant."""
    weight_unit: NotRequired[Nullable[str]]
    r"""The unit of measurement for the weight of the variant."""
    options: NotRequired[List[EcommerceProductVariantsOptionsTypedDict]]
    images: NotRequired[List[EcommerceProductImagesTypedDict]]


class Variants(BaseModel):
    id: OptionalNullable[str] = UNSET
    r"""A unique identifier for the variant of the product."""

    name: OptionalNullable[str] = UNSET
    r"""The name for the variant, used for displaying to customers."""

    price: OptionalNullable[str] = UNSET
    r"""The price of the variant."""

    sku: OptionalNullable[str] = UNSET
    r"""The stock keeping unit of the variant."""

    inventory_quantity: OptionalNullable[str] = UNSET
    r"""The quantity of the variant in stock."""

    weight: OptionalNullable[str] = UNSET
    r"""The weight of the variant."""

    weight_unit: OptionalNullable[str] = UNSET
    r"""The unit of measurement for the weight of the variant."""

    options: Optional[List[EcommerceProductVariantsOptions]] = None

    images: Optional[List[EcommerceProductImages]] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "name",
            "price",
            "sku",
            "inventory_quantity",
            "weight",
            "weight_unit",
            "options",
            "images",
        ]
        nullable_fields = [
            "id",
            "name",
            "price",
            "sku",
            "inventory_quantity",
            "weight",
            "weight_unit",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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


class EcommerceProductCategoriesTypedDict(TypedDict):
    id: NotRequired[Nullable[str]]
    r"""A unique identifier for an object."""
    name: NotRequired[Nullable[str]]
    r"""The name of the category."""


class EcommerceProductCategories(BaseModel):
    id: OptionalNullable[str] = UNSET
    r"""A unique identifier for an object."""

    name: OptionalNullable[str] = UNSET
    r"""The name of the category."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "name"]
        nullable_fields = ["id", "name"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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


class EcommerceProductTypedDict(TypedDict):
    id: str
    r"""A unique identifier for an object."""
    name: NotRequired[Nullable[str]]
    r"""The name of the product as it should be displayed to customers."""
    description: NotRequired[Nullable[str]]
    r"""A detailed description of the product."""
    status: NotRequired[Nullable[ProductStatus]]
    r"""The current status of the product (active or archived)."""
    price: NotRequired[Nullable[str]]
    r"""The price of the product."""
    sku: NotRequired[Nullable[str]]
    r"""The stock keeping unit of the product."""
    inventory_quantity: NotRequired[Nullable[str]]
    r"""The quantity of the product in stock."""
    images: NotRequired[Nullable[List[ImagesTypedDict]]]
    r"""An array of image URLs for the product."""
    weight: NotRequired[Nullable[str]]
    r"""The weight of the product."""
    weight_unit: NotRequired[Nullable[str]]
    r"""The unit of measurement for the weight of the product."""
    options: NotRequired[List[EcommerceProductOptionsTypedDict]]
    r"""An array of options for the product."""
    variants: NotRequired[List[VariantsTypedDict]]
    tags: NotRequired[List[str]]
    r"""An array of tags for the product, used for organization and searching."""
    categories: NotRequired[List[EcommerceProductCategoriesTypedDict]]
    r"""An array of categories for the product, used for organization and searching."""
    custom_mappings: NotRequired[Nullable[CustomMappingsTypedDict]]
    r"""When custom mappings are configured on the resource, the result is included here."""
    created_at: NotRequired[Nullable[datetime]]
    r"""The date and time when the object was created."""
    updated_at: NotRequired[Nullable[datetime]]
    r"""The date and time when the object was last updated."""


class EcommerceProduct(BaseModel):
    id: str
    r"""A unique identifier for an object."""

    name: OptionalNullable[str] = UNSET
    r"""The name of the product as it should be displayed to customers."""

    description: OptionalNullable[str] = UNSET
    r"""A detailed description of the product."""

    status: OptionalNullable[ProductStatus] = UNSET
    r"""The current status of the product (active or archived)."""

    price: OptionalNullable[str] = UNSET
    r"""The price of the product."""

    sku: OptionalNullable[str] = UNSET
    r"""The stock keeping unit of the product."""

    inventory_quantity: OptionalNullable[str] = UNSET
    r"""The quantity of the product in stock."""

    images: OptionalNullable[List[Images]] = UNSET
    r"""An array of image URLs for the product."""

    weight: OptionalNullable[str] = UNSET
    r"""The weight of the product."""

    weight_unit: OptionalNullable[str] = UNSET
    r"""The unit of measurement for the weight of the product."""

    options: Optional[List[EcommerceProductOptions]] = None
    r"""An array of options for the product."""

    variants: Optional[List[Variants]] = None

    tags: Optional[List[str]] = None
    r"""An array of tags for the product, used for organization and searching."""

    categories: Optional[List[EcommerceProductCategories]] = None
    r"""An array of categories for the product, used for organization and searching."""

    custom_mappings: OptionalNullable[CustomMappings] = UNSET
    r"""When custom mappings are configured on the resource, the result is included here."""

    created_at: OptionalNullable[datetime] = UNSET
    r"""The date and time when the object was created."""

    updated_at: OptionalNullable[datetime] = UNSET
    r"""The date and time when the object was last updated."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "name",
            "description",
            "status",
            "price",
            "sku",
            "inventory_quantity",
            "images",
            "weight",
            "weight_unit",
            "options",
            "variants",
            "tags",
            "categories",
            "custom_mappings",
            "created_at",
            "updated_at",
        ]
        nullable_fields = [
            "name",
            "description",
            "status",
            "price",
            "sku",
            "inventory_quantity",
            "images",
            "weight",
            "weight_unit",
            "custom_mappings",
            "created_at",
            "updated_at",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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
