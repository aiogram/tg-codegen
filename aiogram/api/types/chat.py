from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from .base import TelegramObject

if TYPE_CHECKING:  # pragma: no cover
    from .chat_location import ChatLocation
    from .chat_permissions import ChatPermissions
    from .chat_photo import ChatPhoto
    from .message import Message


class Chat(TelegramObject):
    """
    This object represents a chat.

    Source: https://core.telegram.org/bots/api#chat
    """

    id: int
    """Unique identifier for this chat. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier."""
    type: str
    """Type of chat, can be either 'private', 'group', 'supergroup' or 'channel'"""
    title: Optional[str] = None
    """*Optional*. Title, for supergroups, channels and group chats"""
    username: Optional[str] = None
    """*Optional*. Username, for private chats, supergroups and channels if available"""
    first_name: Optional[str] = None
    """*Optional*. First name of the other party in a private chat"""
    last_name: Optional[str] = None
    """*Optional*. Last name of the other party in a private chat"""
    photo: Optional[ChatPhoto] = None
    """*Optional*. Chat photo. Returned only in :class:`aiogram.methods.get_chat.GetChat`."""
    bio: Optional[str] = None
    """*Optional*. Bio of the other party in a private chat. Returned only in :class:`aiogram.methods.get_chat.GetChat`."""
    description: Optional[str] = None
    """*Optional*. Description, for groups, supergroups and channel chats. Returned only in :class:`aiogram.methods.get_chat.GetChat`."""
    invite_link: Optional[str] = None
    """*Optional*. Chat invite link, for groups, supergroups and channel chats. Each administrator in a chat generates their own invite links, so the bot must first generate the link using :class:`aiogram.methods.export_chat_invite_link.ExportChatInviteLink`. Returned only in :class:`aiogram.methods.get_chat.GetChat`."""
    pinned_message: Optional[Message] = None
    """*Optional*. The most recent pinned message (by sending date). Returned only in :class:`aiogram.methods.get_chat.GetChat`."""
    permissions: Optional[ChatPermissions] = None
    """*Optional*. Default chat member permissions, for groups and supergroups. Returned only in :class:`aiogram.methods.get_chat.GetChat`."""
    slow_mode_delay: Optional[int] = None
    """*Optional*. For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user. Returned only in :class:`aiogram.methods.get_chat.GetChat`."""
    sticker_set_name: Optional[str] = None
    """*Optional*. For supergroups, name of group sticker set. Returned only in :class:`aiogram.methods.get_chat.GetChat`."""
    can_set_sticker_set: Optional[bool] = None
    """*Optional*. True, if the bot can change the group sticker set. Returned only in :class:`aiogram.methods.get_chat.GetChat`."""
    linked_chat_id: Optional[int] = None
    """*Optional*. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. Returned only in :class:`aiogram.methods.get_chat.GetChat`."""
    location: Optional[ChatLocation] = None
    """*Optional*. For supergroups, the location to which the supergroup is connected. Returned only in :class:`aiogram.methods.get_chat.GetChat`."""
