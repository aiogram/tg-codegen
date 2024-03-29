from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from .base import TelegramObject

if TYPE_CHECKING:
    pass


class LoginUrl(TelegramObject):
    """
    This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the `Telegram Login Widget <https://core.telegram.org/widgets/login>`_ when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:
    Telegram apps support these buttons as of `version 5.7 <https://telegram.org/blog/privacy-discussions-web-bots#meet-seamless-web-bots>`_.

     Sample bot: `@discussbot <https://t.me/discussbot>`_

    Source: https://core.telegram.org/bots/api#loginurl
    """

    url: str
    """An HTTP URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in `Receiving authorization data <https://core.telegram.org/widgets/login#receiving-authorization-data>`_."""
    forward_text: Optional[str] = None
    """*Optional*. New text of the button in forwarded messages."""
    bot_username: Optional[str] = None
    """*Optional*. Username of a bot, which will be used for user authorization. See `Setting up a bot <https://core.telegram.org/widgets/login#setting-up-a-bot>`_ for more details. If not specified, the current bot's username will be assumed. The *url*'s domain must be the same as the domain linked with the bot. See `Linking your domain to the bot <https://core.telegram.org/widgets/login#linking-your-domain-to-the-bot>`_ for more details."""
    request_write_access: Optional[bool] = None
    """*Optional*. Pass :code:`True` to request the permission for your bot to send messages to the user."""
