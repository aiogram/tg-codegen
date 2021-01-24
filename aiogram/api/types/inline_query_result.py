from __future__ import annotations

from typing import TYPE_CHECKING

from .base import TelegramObject

if TYPE_CHECKING:  # pragma: no cover
    pass


class InlineQueryResult(TelegramObject):
    """
    This object represents one result of an inline query. Telegram clients currently support results of the following 20 types:

     - :class:`aiogram.types.inline_query_result_cached_audio.InlineQueryResultCachedAudio`
     - :class:`aiogram.types.inline_query_result_cached_document.InlineQueryResultCachedDocument`
     - :class:`aiogram.types.inline_query_result_cached_gif.InlineQueryResultCachedGif`
     - :class:`aiogram.types.inline_query_result_cached_mpeg4_gif.InlineQueryResultCachedMpeg4Gif`
     - :class:`aiogram.types.inline_query_result_cached_photo.InlineQueryResultCachedPhoto`
     - :class:`aiogram.types.inline_query_result_cached_sticker.InlineQueryResultCachedSticker`
     - :class:`aiogram.types.inline_query_result_cached_video.InlineQueryResultCachedVideo`
     - :class:`aiogram.types.inline_query_result_cached_voice.InlineQueryResultCachedVoice`
     - :class:`aiogram.types.inline_query_result_article.InlineQueryResultArticle`
     - :class:`aiogram.types.inline_query_result_audio.InlineQueryResultAudio`
     - :class:`aiogram.types.inline_query_result_contact.InlineQueryResultContact`
     - :class:`aiogram.types.inline_query_result_game.InlineQueryResultGame`
     - :class:`aiogram.types.inline_query_result_document.InlineQueryResultDocument`
     - :class:`aiogram.types.inline_query_result_gif.InlineQueryResultGif`
     - :class:`aiogram.types.inline_query_result_location.InlineQueryResultLocation`
     - :class:`aiogram.types.inline_query_result_mpeg4_gif.InlineQueryResultMpeg4Gif`
     - :class:`aiogram.types.inline_query_result_photo.InlineQueryResultPhoto`
     - :class:`aiogram.types.inline_query_result_venue.InlineQueryResultVenue`
     - :class:`aiogram.types.inline_query_result_video.InlineQueryResultVideo`
     - :class:`aiogram.types.inline_query_result_voice.InlineQueryResultVoice`

    Source: https://core.telegram.org/bots/api#inlinequeryresult
    """
