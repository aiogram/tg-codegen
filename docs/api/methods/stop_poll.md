# stopPoll

## Description

Use this method to stop a poll which was sent by the bot. On success, the stopped Poll with the final results is returned.


## Arguments

| Name | Type | Description |
| - | - | - |
| `chat_id` | `#!python3 Union[int, str]` | Unique identifier for the target chat or username of the target channel (in the format @channelusername) |
| `message_id` | `#!python3 int` | Identifier of the original message with the poll |
| `reply_markup` | `#!python3 Optional[InlineKeyboardMarkup]` | Optional. A JSON-serialized object for a new message inline keyboard. |



## Response

Type: `#!python3 Poll`

Description: On success, the stopped Poll with the final results is returned.


## Usage


### As bot method bot

```python3
result: Poll = await bot.stop_poll(...)
```

### Method as object

Imports:

- `from aiogram.types import StopPoll`
- `from aiogram.api.types import StopPoll`
- `from aiogram.api.types.stop_poll import StopPoll`

#### As reply into Webhook
```python3
return StopPoll(...)
```

#### With specific bot
```python3
result: Poll = await bot.emit(StopPoll(...))
```

#### In handlers with current bot
```python3
result: Poll = await StopPoll(...)
```


## Related pages:

- [Official documentation](https://core.telegram.org/bots/api#stoppoll)
- [aiogram.types.InlineKeyboardMarkup](../types/inline_keyboard_markup.md)
- [aiogram.types.Poll](../types/poll.md)
