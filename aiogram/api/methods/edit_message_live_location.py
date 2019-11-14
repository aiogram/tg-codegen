from typing import Any, Dict, Optional, Union

from ..types import InlineKeyboardMarkup, Message
from .base import Request, TelegramMethod


class EditMessageLiveLocation(TelegramMethod[Union[Message, bool]]):
    """
    Use this method to edit live location messages. A location can be edited until its live_period
    expires or editing is explicitly disabled by a call to stopMessageLiveLocation. On success, if
    the edited message was sent by the bot, the edited Message is returned, otherwise True is
    returned.

    Source: https://core.telegram.org/bots/api#editmessagelivelocation
    """

    __returning__ = Union[Message, bool]

    latitude: float
    """Latitude of new location"""
    longitude: float
    """Longitude of new location"""
    chat_id: Optional[Union[int, str]] = None
    """Required if inline_message_id is not specified. Unique identifier for the target chat or
    username of the target channel (in the format @channelusername)"""
    message_id: Optional[int] = None
    """Required if inline_message_id is not specified. Identifier of the message to edit"""
    inline_message_id: Optional[str] = None
    """Required if chat_id and message_id are not specified. Identifier of the inline message"""
    reply_markup: Optional[InlineKeyboardMarkup] = None
    """A JSON-serialized object for a new inline keyboard."""

    def build_request(self) -> Request:
        data: Dict[str, Any] = self.dict()

        return Request(method="editMessageLiveLocation", data=data)
