from .base import TelegramMethod
from .get_updates import GetUpdates
from .set_webhook import SetWebhook
from .delete_webhook import DeleteWebhook
from .get_webhook_info import GetWebhookInfo
from .get_me import GetMe
from .send_message import SendMessage
from .forward_message import ForwardMessage
from .send_photo import SendPhoto
from .send_audio import SendAudio
from .send_document import SendDocument
from .send_video import SendVideo
from .send_animation import SendAnimation
from .send_voice import SendVoice
from .send_video_note import SendVideoNote
from .send_media_group import SendMediaGroup
from .send_location import SendLocation
from .edit_message_live_location import EditMessageLiveLocation
from .stop_message_live_location import StopMessageLiveLocation
from .send_venue import SendVenue
from .send_contact import SendContact
from .send_poll import SendPoll
from .send_chat_action import SendChatAction
from .get_user_profile_photos import GetUserProfilePhotos
from .get_file import GetFile
from .kick_chat_member import KickChatMember
from .unban_chat_member import UnbanChatMember
from .restrict_chat_member import RestrictChatMember
from .promote_chat_member import PromoteChatMember
from .set_chat_permissions import SetChatPermissions
from .export_chat_invite_link import ExportChatInviteLink
from .set_chat_photo import SetChatPhoto
from .delete_chat_photo import DeleteChatPhoto
from .set_chat_title import SetChatTitle
from .set_chat_description import SetChatDescription
from .pin_chat_message import PinChatMessage
from .unpin_chat_message import UnpinChatMessage
from .leave_chat import LeaveChat
from .get_chat import GetChat
from .get_chat_administrators import GetChatAdministrators
from .get_chat_members_count import GetChatMembersCount
from .get_chat_member import GetChatMember
from .set_chat_sticker_set import SetChatStickerSet
from .delete_chat_sticker_set import DeleteChatStickerSet
from .answer_callback_query import AnswerCallbackQuery
from .edit_message_text import EditMessageText
from .edit_message_caption import EditMessageCaption
from .edit_message_media import EditMessageMedia
from .edit_message_reply_markup import EditMessageReplyMarkup
from .stop_poll import StopPoll
from .delete_message import DeleteMessage
from .send_sticker import SendSticker
from .get_sticker_set import GetStickerSet
from .upload_sticker_file import UploadStickerFile
from .create_new_sticker_set import CreateNewStickerSet
from .add_sticker_to_set import AddStickerToSet
from .set_sticker_position_in_set import SetStickerPositionInSet
from .delete_sticker_from_set import DeleteStickerFromSet
from .answer_inline_query import AnswerInlineQuery
from .send_invoice import SendInvoice
from .answer_shipping_query import AnswerShippingQuery
from .answer_pre_checkout_query import AnswerPreCheckoutQuery
from .set_passport_data_errors import SetPassportDataErrors
from .send_game import SendGame
from .set_game_score import SetGameScore
from .get_game_high_scores import GetGameHighScores

__all__ = (
    "TelegramMethod",
    "GetUpdates",
    "SetWebhook",
    "DeleteWebhook",
    "GetWebhookInfo",
    "GetMe",
    "SendMessage",
    "ForwardMessage",
    "SendPhoto",
    "SendAudio",
    "SendDocument",
    "SendVideo",
    "SendAnimation",
    "SendVoice",
    "SendVideoNote",
    "SendMediaGroup",
    "SendLocation",
    "EditMessageLiveLocation",
    "StopMessageLiveLocation",
    "SendVenue",
    "SendContact",
    "SendPoll",
    "SendChatAction",
    "GetUserProfilePhotos",
    "GetFile",
    "KickChatMember",
    "UnbanChatMember",
    "RestrictChatMember",
    "PromoteChatMember",
    "SetChatPermissions",
    "ExportChatInviteLink",
    "SetChatPhoto",
    "DeleteChatPhoto",
    "SetChatTitle",
    "SetChatDescription",
    "PinChatMessage",
    "UnpinChatMessage",
    "LeaveChat",
    "GetChat",
    "GetChatAdministrators",
    "GetChatMembersCount",
    "GetChatMember",
    "SetChatStickerSet",
    "DeleteChatStickerSet",
    "AnswerCallbackQuery",
    "EditMessageText",
    "EditMessageCaption",
    "EditMessageMedia",
    "EditMessageReplyMarkup",
    "StopPoll",
    "DeleteMessage",
    "SendSticker",
    "GetStickerSet",
    "UploadStickerFile",
    "CreateNewStickerSet",
    "AddStickerToSet",
    "SetStickerPositionInSet",
    "DeleteStickerFromSet",
    "AnswerInlineQuery",
    "SendInvoice",
    "AnswerShippingQuery",
    "AnswerPreCheckoutQuery",
    "SetPassportDataErrors",
    "SendGame",
    "SetGameScore",
    "GetGameHighScores",
)
