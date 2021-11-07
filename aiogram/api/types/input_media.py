from __future__ import annotations

from typing import TYPE_CHECKING

from .base import TelegramObject

if TYPE_CHECKING:
    pass


class InputMedia(TelegramObject):
    """
    This object represents the content of a media message to be sent. It should be one of

     - :class:`aiogram.types.input_media_animation.InputMediaAnimation`
     - :class:`aiogram.types.input_media_document.InputMediaDocument`
     - :class:`aiogram.types.input_media_audio.InputMediaAudio`
     - :class:`aiogram.types.input_media_photo.InputMediaPhoto`
     - :class:`aiogram.types.input_media_video.InputMediaVideo`

    Source: https://core.telegram.org/bots/api#inputmedia
    """
