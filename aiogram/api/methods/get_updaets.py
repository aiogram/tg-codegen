from typing import Optional, List, Dict, Any

from aiogram.api.methods.base import TelegramMethod, Request, Response
from aiogram.types import Update


class GetUpdates(TelegramMethod):
    offset: Optional[int] = None
    limit: Optional[int] = None
    timeout: Optional[int] = None
    allowed_updates: Optional[List[str]] = None

    def build_request(self) -> Request:
        return Request(method="getUpdates", data=self.dict(exclude_unset=True))

    def build_response(self, data: Dict[str, Any]) -> Response[List[Update]]:
        return Response[List[Update]](**data)
