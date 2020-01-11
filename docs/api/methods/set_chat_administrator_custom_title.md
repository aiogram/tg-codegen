# setChatAdministratorCustomTitle

## Description

Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns True on success.


## Arguments

| Name | Type | Description |
| - | - | - |
| `chat_id` | `#!python3 Union[int, str]` | Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername) |
| `user_id` | `#!python3 int` | Unique identifier of the target user |
| `custom_title` | `#!python3 str` | New custom title for the administrator; 0-16 characters, emoji are not allowed |



## Response

Type: `#!python3 bool`

Description: Returns True on success.


## Usage


### As bot method bot

```python3
result: bool = await bot.set_chat_administrator_custom_title(...)
```

### Method as object

Imports:

- `from aiogram.types import SetChatAdministratorCustomTitle`
- `from aiogram.api.types import SetChatAdministratorCustomTitle`
- `from aiogram.api.types.set_chat_administrator_custom_title import SetChatAdministratorCustomTitle`

#### As reply into Webhook
```python3
return SetChatAdministratorCustomTitle(...)
```

#### With specific bot
```python3
result: bool = await bot.emit(SetChatAdministratorCustomTitle(...))
```

#### In handlers with current bot
```python3
result: bool = await SetChatAdministratorCustomTitle(...)
```


## Related pages:

- [Official documentation](https://core.telegram.org/bots/api#setchatadministratorcustomtitle)
