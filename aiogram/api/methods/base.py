import abc
import io
from typing import Dict, Union, Optional, TypeVar, Generic, Any

from pydantic import BaseModel, BaseConfig, Extra
from pydantic.generics import GenericModel

from aiogram.api.types import InputFile, ResponseParameters

T = TypeVar("T")


class Request(BaseModel):
    method: str

    data: Dict[str, Union[str, int, bool]]
    files: Optional[Dict[str, Union[io.BytesIO, bytes, InputFile]]]

    class Config(BaseConfig):
        arbitrary_types_allowed = True


class Response(ResponseParameters, GenericModel, Generic[T]):
    ok: bool
    result: Optional[T] = None
    description: Optional[str] = None
    error_code: Optional[int] = None


class TelegramMethod(abc.ABC, BaseModel):
    class Config(BaseConfig):
        use_enum_values = True
        orm_mode = True
        extra = Extra.allow
        allow_mutation = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

    @abc.abstractmethod
    def build_request(self) -> Request:
        pass

    @abc.abstractmethod
    def build_response(self, data: Dict[str, Any]) -> Response[T]:
        pass
