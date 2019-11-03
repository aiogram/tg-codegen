from typing import Any, TypeVar

from aiogram.api import methods

T = TypeVar("T")


class BaseBot:
    def __init__(self):
        self.session = None

    async def emit(self, method: methods.TelegramMethod) -> Any:
        request = method.build_request()
        raw_response = await self.session.make_request(request)
        response = method.build_response(raw_response)
        return response.result
