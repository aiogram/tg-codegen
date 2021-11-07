from __future__ import annotations

from typing import TYPE_CHECKING

from .base import TelegramObject

if TYPE_CHECKING:
    pass


class MessageId(TelegramObject):
    """
    This object represents a unique message identifier.

    Source: https://core.telegram.org/bots/api#messageid
    """

    message_id: int
    """Unique message identifier"""
