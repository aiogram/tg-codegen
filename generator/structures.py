from __future__ import annotations

import functools
import typing
from dataclasses import dataclass, field

from generator.normalizers import get_returning, normalize_optional, normalize_type, pythonize_name


@dataclass
class Annotation:
    name: str
    type: str
    description: str
    required: bool = True
    const: typing.Optional[str] = None

    @property
    def python_default_value(self) -> typing.Optional[str]:
        if self.name in {"parse_mode", "explanation_parse_mode"}:
            default_value = "UNSET"
        elif not self.required:
            default_value = "None"
        else:
            default_value = None
        return default_value

    @property
    def python_name(self):
        if self.name == "from":
            return "from_user"
        return self.name

    @property
    def python_type(self) -> str:
        result = normalize_type(self.type)
        if self.name == "date":
            return normalize_optional("datetime.datetime", required=self.required)
        if self.name == "media" and result == "str":
            return normalize_optional("Union[str, InputFile]", required=self.required)
        if self.name in {"until_date", "close_date"}:
            return normalize_optional(
                "Union[datetime.datetime, datetime.timedelta, int]", required=self.required
            )
        return normalize_optional(result, self.required)

    @property
    def python_field(self) -> str:
        result = f"{self.python_name}: {self.python_type}"

        value = self.python_default_value
        if self.name == "from":
            value = f"Field({value or '...'}, alias=\"from\")"
        elif self.name in {"parse_mode", "explanation_parse_mode"}:
            value = "UNSET"
        elif self.const:
            value = f"Field({self.const!r}, const=True)"
        if value:
            result += f" = {value}"
        return result


@dataclass
class Entity:
    name: str
    anchor: str
    description: str = None
    annotations: typing.List[Annotation] = field(default_factory=list)

    extends: typing.Optional[typing.List[str]] = None

    def fix_annotations_ordering(self):
        if not self.annotations:
            return
        required_annotations = []
        not_required_annotations = []
        for annotation in self.annotations:
            if annotation.required:
                required_annotations.append(annotation)
            else:
                not_required_annotations.append(annotation)

        self.annotations = required_annotations + not_required_annotations

    @property
    def is_method(self) -> bool:
        return self.name[0].islower()

    @property
    def is_type(self) -> bool:
        return not self.is_method

    @property
    def pythonic_name(self) -> str:
        return pythonize_name(self.name)

    def _get_returning(self):
        if self.is_type:
            return self.name, ""

        return get_returning(self.description)

    @property
    def returning(self):
        return self._get_returning()[1]

    @property
    def returning_type(self):
        return self._get_returning()[0]

    @property
    def python_returning_type(self):
        return normalize_type(self.returning_type)

    @property
    def file_annotations(self):
        result = []
        for item in self.annotations:
            if "InputFile" in item.python_type:
                result.append(item)
        return result

    @property
    def parse_mode_annotations(self):
        parse_mode = None
        entities = None

        for entity in self.annotations:
            if entity.name.endswith("parse_mode"):
                parse_mode = entity.name
            elif entity.name.endswith("entities"):
                entities = entity.name
        return parse_mode, entities

    @property
    def can_be_used_in_webhook(self):
        if self.is_type:
            return False
        if self.name.startswith("get"):
            return False
        for annotation in self.annotations:
            if annotation.python_type == "InputFile":
                return False
        return True


@dataclass
class Group:
    title: str
    anchor: str
    description: str = None
    childs: typing.List[Entity] = field(default_factory=list)

    @property
    def has_methods(self):
        return any(entity.is_method for entity in self.childs)

    @property
    def has_types(self):
        return any(entity.is_type for entity in self.childs)
