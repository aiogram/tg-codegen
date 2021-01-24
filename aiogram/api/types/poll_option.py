from __future__ import annotations

from typing import TYPE_CHECKING

from .base import TelegramObject

if TYPE_CHECKING:  # pragma: no cover
    pass


class PollOption(TelegramObject):
    """
    This object contains information about one answer option in a poll.

    Source: https://core.telegram.org/bots/api#polloption
    """

    text: str
    """Option text, 1-100 characters"""
    voter_count: int
    """Number of users that voted for this option"""
