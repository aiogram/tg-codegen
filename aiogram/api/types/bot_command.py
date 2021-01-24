from __future__ import annotations

from typing import TYPE_CHECKING

from .base import TelegramObject

if TYPE_CHECKING:  # pragma: no cover
    pass


class BotCommand(TelegramObject):
    """
    This object represents a bot command.

    Source: https://core.telegram.org/bots/api#botcommand
    """

    command: str
    """Text of the command, 1-32 characters. Can contain only lowercase English letters, digits and underscores."""
    description: str
    """Description of the command, 3-256 characters."""
