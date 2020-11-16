from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from .base import UNSET
from .input_message_content import InputMessageContent

if TYPE_CHECKING:  # pragma: no cover
    from .message_entity import MessageEntity


class InputTextMessageContent(InputMessageContent):
    """
    Represents the content of a text message to be sent as the result of an inline query.

    Source: https://core.telegram.org/bots/api#inputtextmessagecontent
    """

    message_text: str
    """Text of the message to be sent, 1-4096 characters"""
    parse_mode: Optional[str] = UNSET
    """Mode for parsing entities in the message text. See formatting options for more details."""
    entities: Optional[List[MessageEntity]] = None
    """List of special entities that appear in message text, which can be specified instead of
    parse_mode"""
    disable_web_page_preview: Optional[bool] = None
    """Disables link previews for links in the sent message"""
