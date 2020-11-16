from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

from ..types import (
    UNSET,
    ForceReply,
    InlineKeyboardMarkup,
    InputFile,
    Message,
    MessageEntity,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from .base import Request, TelegramMethod, prepare_file, prepare_parse_mode

if TYPE_CHECKING:  # pragma: no cover
    from ..client.bot import Bot


class SendPhoto(TelegramMethod[Message]):
    """
    Use this method to send photos. On success, the sent Message is returned.

    Source: https://core.telegram.org/bots/api#sendphoto
    """

    __returning__ = Message

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target channel (in the format
    @channelusername)"""
    photo: Union[InputFile, str]
    """Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers
    (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet,
    or upload a new photo using multipart/form-data."""
    caption: Optional[str] = None
    """Photo caption (may also be used when resending photos by file_id), 0-1024 characters after
    entities parsing"""
    parse_mode: Optional[str] = UNSET
    """Mode for parsing entities in the photo caption. See formatting options for more details."""
    caption_entities: Optional[List[MessageEntity]] = None
    """List of special entities that appear in the caption, which can be specified instead of
    parse_mode"""
    disable_notification: Optional[bool] = None
    """Sends the message silently. Users will receive a notification with no sound."""
    reply_to_message_id: Optional[int] = None
    """If the message is a reply, ID of the original message"""
    allow_sending_without_reply: Optional[bool] = None
    """Pass True, if the message should be sent even if the specified replied-to message is not
    found"""
    reply_markup: Optional[
        Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
    ] = None
    """Additional interface options. A JSON-serialized object for an inline keyboard, custom reply
    keyboard, instructions to remove reply keyboard or to force a reply from the user."""

    def build_request(self, bot: Bot) -> Request:
        data: Dict[str, Any] = self.dict(exclude={"photo"})

        prepare_parse_mode(
            bot, data, parse_mode_property="parse_mode", entities_property="caption_entities"
        )

        files: Dict[str, InputFile] = {}
        prepare_file(data=data, files=files, name="photo", value=self.photo)

        return Request(method="sendPhoto", data=data, files=files)
