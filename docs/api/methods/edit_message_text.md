# editMessageText

## Description

Use this method to edit text and game messages. On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.


## Arguments

| Name | Type | Description |
| - | - | - |
| `text` | `#!python3 str` | New text of the message |
| `chat_id` | `#!python3 Optional[Union[int, str]]` | Optional. Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername) |
| `message_id` | `#!python3 Optional[int]` | Optional. Required if inline_message_id is not specified. Identifier of the message to edit |
| `inline_message_id` | `#!python3 Optional[str]` | Optional. Required if chat_id and message_id are not specified. Identifier of the inline message |
| `parse_mode` | `#!python3 Optional[str]` | Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message. |
| `disable_web_page_preview` | `#!python3 Optional[bool]` | Optional. Disables link previews for links in this message |
| `reply_markup` | `#!python3 Optional[InlineKeyboardMarkup]` | Optional. A JSON-serialized object for an inline keyboard. |



## Response

Type: `#!python3 Union[Message, bool]`

Description: On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.


## Usage


### As bot method bot

```python3
result: Union[Message, bool] = await bot.edit_message_text(...)
```

### Method as object

Imports:

- `from aiogram.types import EditMessageText`
- `from aiogram.api.types import EditMessageText`
- `from aiogram.api.types.edit_message_text import EditMessageText`

#### As reply into Webhook
```python3
return EditMessageText(...)
```

#### With specific bot
```python3
result: Union[Message, bool] = await bot.emit(EditMessageText(...))
```

#### In handlers with current bot
```python3
result: Union[Message, bool] = await EditMessageText(...)
```


## Related pages:

- [Official documentation](https://core.telegram.org/bots/api#editmessagetext)
- [aiogram.types.InlineKeyboardMarkup](../types/inline_keyboard_markup.md)
- [aiogram.types.Message](../types/message.md)
