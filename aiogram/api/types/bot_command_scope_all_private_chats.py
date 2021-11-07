from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from .bot_command_scope import BotCommandScope

if TYPE_CHECKING:
    pass


class BotCommandScopeAllPrivateChats(BotCommandScope):
    """
    Represents the `scope <https://core.telegram.org/bots/api#botcommandscope>`_ of bot commands, covering all private chats.

    Source: https://core.telegram.org/bots/api#botcommandscopeallprivatechats
    """

    type: str = Field("all_private_chats", const=True)
    """Scope type, must be *all_private_chats*"""
